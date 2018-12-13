from cdwtraficoaereo.cfg.constants import InputFileTypes
from cdwtraficoaereo.fw import Factory


class UniversalFactory(Factory):

    @staticmethod
    def build(*args, **kwargs):
        pass


class DataLoaderFactory(UniversalFactory):

    @staticmethod
    def build(loader_type):

        from cdwtraficoaereo.components.loader import CsvDataLoader, JsonDataLoader, XmlDataLoader

        loader = {
            InputFileTypes.CSV: CsvDataLoader()
            , InputFileTypes.JSON: JsonDataLoader()
            , InputFileTypes.XML: XmlDataLoader()

        }[loader_type]

        return loader


class PipelineFactory(UniversalFactory):

    @staticmethod
    def build():

        from cdwtraficoaereo.pipeline.run import EtlPipelineRunner

        return EtlPipelineRunner()
