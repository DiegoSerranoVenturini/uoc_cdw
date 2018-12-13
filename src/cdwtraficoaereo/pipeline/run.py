import logging

from cdwtraficoaereo.fw import PipelineRunner
from cdwtraficoaereo.factories import DataLoaderFactory
from cdwtraficoaereo.helpers.spark import SparkSessionFactory
from cdwtraficoaereo.helpers.database import DatabaseManager

log = logging.getLogger(__name__)


class EtlPipelineRunner(PipelineRunner):

    def run_etl_pipeline(self, sources):

        spark = self._initialize_engine()

        sources_raw_data = {}
        for source in sources:
            source_name = source["name"]
            source_type = source["type"]
            source_path = source["path"]
            source_args = source["args"]

            loader = DataLoaderFactory.build(source_type)

            raw_data = loader.load_data(spark, source_path, **source_args)
            sources_raw_data[source_name] = raw_data

    @staticmethod
    def _initialize_engine():

        spark = SparkSessionFactory.get_spark()

        try:
            DatabaseManager.use_database(spark)

        except Exception as e:
            log.error(e)

            log.info("Creating database...")
            DatabaseManager.create_database(spark)

            DatabaseManager.use_database(spark)

        return spark
