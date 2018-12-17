class ApplicationConstants:
    pass


class DatabaseConstants(ApplicationConstants):

    DATABASE_NAME = "cdw_trafico_aereo"


class InputFileTypes(ApplicationConstants):

    CSV = "csv"
    JSON = "json"
    XML = "xml"


class FilePathConstants(ApplicationConstants):

    RAW_DATA_FOLDER = "/Users/diegoserrano/prj/uoc/cdw/caso_practico1/PRA1-Datos"
    THIRD_PARTIE_FOLDER = "/Users/diegoserrano/third-parties"


class SourceNames(ApplicationConstants):

    AIRLINES = "airlines"
    AIRPORTS = "airports"
    ROUTES = "routes"
    ROUTE_TYPE = "route_type"
    EQUIPMENT = "equipment"
    COUNTRIES = "countries"
    PASS_COUNTRY = "pass_country"
    COM_COUNTRY = "com_country"
    POP_COUNTRY = "pop_country"
    TOUR_COUNTRY = "tour_country"
