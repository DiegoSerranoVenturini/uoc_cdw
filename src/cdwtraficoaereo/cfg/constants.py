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
