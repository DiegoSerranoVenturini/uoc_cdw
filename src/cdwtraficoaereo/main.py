import sys
from cdwtraficoaereo.factories import PipelineFactory
from cdwtraficoaereo.cfg.constants import FilePathConstants


def run_application(argv):

    pipeline = PipelineFactory.build()

    sources = [
        {
            "path": FilePathConstants.RAW_DATA_FOLDER + "/airlines.dat"
            , "type": "csv"
            , "name": "airlines"
            , "args":
            {
                "header": False
            }
        },
        {
            "path": FilePathConstants.RAW_DATA_FOLDER + "/equipamientos.js"
            , "type": "json"
            , "name": "equipment"
            , "args": {}
        },
        {
            "path": FilePathConstants.RAW_DATA_FOLDER + "/paises.xml"
            , "type": "xml"
            , "name": "countries"
            , "args": {"row_tag": "row"}
        }
    ]

    pipeline.run_etl_pipeline(sources=sources)


if __name__ == '__main__':

    args = sys.argv

    run_application(args)


