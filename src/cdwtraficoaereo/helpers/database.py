import logging
from cdwtraficoaereo.cfg.constants import DatabaseConstants
from pyspark.sql import SparkSession

log = logging.getLogger(__name__)


class DatabaseManager:

    @staticmethod
    def create_database(spark: SparkSession, database_name=DatabaseConstants.DATABASE_NAME):
        try:
            spark.sql("CREATE DATABASE IF NOT EXISTS {}".format(database_name))
        except Exception as e:
            log.error(e)

    @staticmethod
    def use_database(spark: SparkSession, database_name=DatabaseConstants.DATABASE_NAME):
        spark.sql("USE {}".format(database_name))
