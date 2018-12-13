from cdwtraficoaereo.cfg.constants import FilePathConstants
from pyspark.sql import SparkSession


class SparkSessionFactory:

    _spark = None

    @classmethod
    def get_spark(cls):

        if cls._spark is None:
            spark = SparkSession.builder.master("local[*]").appName("cdw-etl"). \
                config("spark.jars", FilePathConstants.THIRD_PARTIE_FOLDER + "/spark-xml/target/scala-2.11/spark-xml_2.11-0.4.2.jar").\
                enableHiveSupport().getOrCreate()
            spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")

            cls._spark = spark

        return cls._spark
