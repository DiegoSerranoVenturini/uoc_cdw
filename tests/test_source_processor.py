from cdwtraficoaereo.components.sources import SourceVault


def test_source_vault_init():

    argv = ["test_source_processor.py", "--sources", "/Users/diegoserrano/prj/uoc/cdw/conf/sources.json"]

    SourceVault.build_from_arguments(argv)

    sources_list = SourceVault().get_sources_list()

    assert isinstance(sources_list, list)

