from pyspark.sql import DataFrame, functions as F
from pyspark.sql.window import *
from cdwtraficoaereo.fw import SourceProcessor
from cdwtraficoaereo.helpers.spark import SparkSessionFactory


class UniversalSourceProcessor(SourceProcessor):

    def process(self, raw_df: DataFrame, *args):

        processed_df = self._impute_nulls(raw_df)

        processed_df = self._apply_custom_pipeline(processed_df)

        processed_df.createOrReplaceTempView("pro_" + self.source.name)

        return processed_df

    def _impute_nulls(self, raw_df: DataFrame):
        source_args = self.source.args

        if isinstance(source_args, dict) and "impute" in source_args.keys():

            imputation_value = source_args["impute"]
            return raw_df.fillna(imputation_value)

        else:
            return raw_df

    def _apply_custom_pipeline(self, raw_df: DataFrame):
        return raw_df


class CountriesSourceProcessor(UniversalSourceProcessor):

    def _apply_custom_pipeline(self, raw_df: DataFrame):
        raw_df = raw_df.\
            withColumn("longitud", F.round(F.col("longitud"), 2)).\
            withColumn("latitud", F.round(F.col("latitud"), 2))

        return raw_df.dropDuplicates()


class EquipmentSourceProcessor(UniversalSourceProcessor):

    def _apply_custom_pipeline(self, raw_df: DataFrame):

        raw_df = raw_df.withColumn("equipamientos", F.explode(raw_df.equipamientos))
        raw_df = raw_df.\
            select(raw_df.equipamientos.cod_equipamiento.alias("cod_equipamiento"),
                   raw_df.equipamientos.desc_equipamiento.alias("desc_equipamiento"))

        return raw_df.dropDuplicates()


class AirlinesSourceProcessor(UniversalSourceProcessor):

    def _apply_custom_pipeline(self, raw_df: DataFrame):
        spark = SparkSessionFactory.get_spark()

        countries = spark.sql("SELECT DISTINCT pais, cod_pais FROM pro_countries")

        raw_df = countries.join(raw_df, on="pais", how="inner").\
            withColumn("id_aerolinea", F.col("openfligths_ID")).\
            withColumn("nombre_aerolinea", F.col("nombre")).\
            withColumn("alias_aerolinea", F.col("alias")).\
            withColumn("cod_iata", F.col("codigo_IATA")).\
            withColumn("cod_icao", F.col("codigo_ICAO")).\
            withColumn("identificacion", F.col("callsign")).\
            withColumn("sw_activa", F.col("Activo")).\
            select(["id_aerolinea", "nombre_aerolinea", "alias_aerolinea", "cod_iata", "cod_icao",
                    "cod_icao", "identificacion", "sw_activa", "cod_pais"])

        return raw_df.dropDuplicates()


class AirportsSourceProcessor(UniversalSourceProcessor):

    def _apply_custom_pipeline(self, raw_df: DataFrame):

        spark = SparkSessionFactory.get_spark()

        countries = spark.sql("SELECT DISTINCT pais, cod_pais FROM pro_countries")

        raw_df = countries.join(raw_df, on="pais", how="inner"). \
            withColumn("longitud", F.round(F.col("longitud"), 2)). \
            withColumn("latitud", F.round(F.col("latitud"), 2)). \
            select(["id_aeropuerto", "nombre_aeropuerto", "ciudad_aeropuerto", "cod_pais", "cod_iata_faa", "cod_icao", "latitud",
                    "longitud", "altitud", "zona_horaria", "dst", "zona_horaria_tz"])

        return raw_df.dropDuplicates()


class RoutesSourceProcessor(UniversalSourceProcessor):

    def _apply_custom_pipeline(self, raw_df: DataFrame):

        spark = SparkSessionFactory.get_spark()

        airports = spark.sql("SELECT DISTINCT id_aeropuerto, cod_pais FROM pro_airports")
        airlines = spark.sql("SELECT DISTINCT id_aerolinea FROM pro_airlines")

        # TODO: divide the equipment column to populate relation table
        routes_df = raw_df.\
            withColumn("id_aeropuerto_ori", F.col("id_aeropuerto_origen").cast("int")).\
            withColumn("id_aeropuerto_des", F.col("id_aeropuerto_destino").cast("int")).\
            join(airports.withColumn("id_aeropuerto_ori", F.col("id_aeropuerto")).withColumn("cod_pais_origen", F.col("cod_pais")),
                 how="inner", on="id_aeropuerto_ori").\
            join(airports.withColumn("id_aeropuerto_des", F.col("id_aeropuerto")).withColumn("cod_pais_destino", F.col("cod_pais")),
                 how="inner", on="id_aeropuerto_des").\
            join(airlines, on="id_aerolinea", how="inner").\
            withColumn("tipo_ruta", F.expr("IF (cod_pais_origen = cod_pais_destino, 'Nacional', 'Internacional')")).\
            withColumn("aeropuerto_ori", F.col("cod_aeropuerto_origen")).\
            withColumn("aeropuerto_des", F.col("cod_aeropuerto_destino")).\
            withColumn("equipamiento_total", F.col("equipamiento")).\
            select(["tipo_ruta", "aeropuerto_ori", "aeropuerto_des", "id_aeropuerto_ori", "id_aeropuerto_des",
                    "equipamiento_total", "num_stops", "id_codeshare", "id_aerolinea"]).\
            dropDuplicates().\
            withColumn("id_ruta", F.row_number().over(Window.orderBy("id_aeropuerto_ori")))

        print(raw_df)

        return routes_df
