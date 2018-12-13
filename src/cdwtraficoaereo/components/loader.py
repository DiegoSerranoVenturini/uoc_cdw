import abc
from pyspark.sql import SparkSession

from cdwtraficoaereo.fw import DataLoader


class UniversalDataLoader(DataLoader):

    def load_data(self, *args, **kwargs):
        raw_data = self._load_data(*args, **kwargs)
        return raw_data

    @abc.abstractmethod
    def _load_data(self, *args, **kwargs):
        pass


class CsvDataLoader(UniversalDataLoader):

    def _load_data(self, spark: SparkSession, path: str, header=True, infer_schema=True, colnames=None):
        raw_data = spark.read.option("header", header).option("inferSchema", infer_schema).csv(path)

        return raw_data


class JsonDataLoader(UniversalDataLoader):

    def _load_data(self, spark: SparkSession, path: str, header=True, infer_schema=True, sep=",", encoding="latin1"):
        raw_data = spark.read.json(path)

        # TODO:
        #  preprocessing:
        #  json_temp = raw_data.withColumn("equipamientos", explode(raw_data.equipamientos))
        #  json_temp.select(
        #      json_temp.equipamientos.cod_equipamiento.alias("cod_equipamiento"),
        #      json_temp.equipamientos.desc_equipamiento.alias("desc_equipamiento"))

        return raw_data


class XmlDataLoader(UniversalDataLoader):

    def _load_data(self, spark: SparkSession, path: str, header=True, infer_schema=True, sep=",", encoding="latin1", row_tag="row"):
        raw_data = spark.read.format("com.databricks.spark.xml").load(path, rowTag=row_tag)

        return raw_data
