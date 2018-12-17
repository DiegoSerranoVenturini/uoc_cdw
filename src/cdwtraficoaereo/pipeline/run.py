import logging

from cdwtraficoaereo.fw import PipelineRunner
from cdwtraficoaereo.factories import DataLoaderFactory, SourceProcessorFactory
from cdwtraficoaereo.helpers.spark import SparkSessionFactory
from cdwtraficoaereo.helpers.database import DatabaseManager

log = logging.getLogger(__name__)


class EtlPipelineRunner(PipelineRunner):

    def run_etl_pipeline(self, sources):

        spark = self._initialize_engine()

        sources_raw_data = {}
        sources_processed_data = {}
        for source in sources:

            loader = DataLoaderFactory.build(source.type)
            raw_data = loader.load_data(spark, source.path, **source.args)

            sources_raw_data[source.name] = raw_data

            source_processor = SourceProcessorFactory().build(source)
            processed_data = source_processor.process(raw_data)

            sources_processed_data[source.name] = processed_data

    @staticmethod
    def _initialize_engine():

        spark = SparkSessionFactory.get_spark()

        try:
            DatabaseManager.use_database(spark)

        except Exception as e:
            log.error(e)

            DatabaseManager.create_database(spark)

            DatabaseManager.use_database(spark)

        return spark
