from cdwtraficoaereo.cfg.constants import InputFileTypes, SourceNames
from cdwtraficoaereo.fw import Factory, SourceProcessor


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


class SourceProcessorFactory(UniversalFactory):

    @staticmethod
    def build(source) -> SourceProcessor:

        from cdwtraficoaereo.components.sources import CountriesSourceProcessor, AirlinesSourceProcessor, UniversalSourceProcessor, \
            EquipmentSourceProcessor, AirportsSourceProcessor, RoutesSourceProcessor

        processor = {
             SourceNames.AIRLINES: AirlinesSourceProcessor(),
             SourceNames.AIRPORTS: AirportsSourceProcessor(),
             SourceNames.ROUTES: RoutesSourceProcessor(),
             SourceNames.ROUTE_TYPE: UniversalSourceProcessor(),
             SourceNames.EQUIPMENT: EquipmentSourceProcessor(),
             SourceNames.COUNTRIES: CountriesSourceProcessor(),
             SourceNames.PASS_COUNTRY: None,
             SourceNames.COM_COUNTRY: None,
             SourceNames.POP_COUNTRY: None,
             SourceNames.TOUR_COUNTRY: None,
        }[source.name]

        processor.set_source(source)

        return processor
