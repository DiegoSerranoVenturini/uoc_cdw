import sys
from cdwtraficoaereo.factories import PipelineFactory
from cdwtraficoaereo.components.sources import SourceVault
from cdwtraficoaereo.cfg.constants import FilePathConstants


def run_application(argv):

    pipeline = PipelineFactory.build()

    SourceVault.build_from_arguments(argv)

    sources_list = SourceVault().get_sources_list()

    pipeline.run_etl_pipeline(sources=sources_list)


if __name__ == '__main__':

    args = sys.argv

    run_application(args)


