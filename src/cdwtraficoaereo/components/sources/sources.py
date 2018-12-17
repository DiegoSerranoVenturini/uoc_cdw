import argparse
import json
import os
from cdwtraficoaereo.helpers.common import Singleton


class Source(dict):

    KEY_NAME = "name"
    KEY_TYPE = "type"
    KEY_PATH = "path"
    KEY_ARGS = "args"

    KEYS = [KEY_NAME, KEY_TYPE, KEY_PATH, KEY_ARGS]

    def get(self, key):
        if key in self.KEYS:
            return self[key]
        else:
            return None

    @property
    def name(self):
        return self.get(self.KEY_NAME)

    @property
    def type(self):
        return self.get(self.KEY_TYPE)

    @property
    def path(self):
        return self.get(self.KEY_PATH)

    @property
    def args(self):
        return self.get(self.KEY_ARGS)


class SourceVault(Singleton):

    SOURCE_ARGUMENT = "sources"
    SOURCE_LIST = []

    @classmethod
    def build_from_arguments(cls, argv):

        argument_dictionary = cls.parse_input_arguments_into_dict(argv, [cls.SOURCE_ARGUMENT])

        sources_dictionaries = cls.parse_json_file_arg_to_dict(argument_dictionary[cls.SOURCE_ARGUMENT])

        cls.SOURCE_LIST = [Source(**source_dict) for source_dict in sources_dictionaries]

    def get_sources_list(self):
        return self.SOURCE_LIST

    @staticmethod
    def parse_input_arguments_into_dict(argv, argument_list=None) -> dict:
        """
        Parses the arguments from the command line into a dictionary
        Will ignore unknown arguments i.e. not explicitly passed to the argument list
        :param argv: The input string from the command line
        :param argument_list: List of the argument name such as --experiment, --feature. Should not prefix by --
        :return: dictionary with argument names as dict keys and argument values as dict values
        """
        if argument_list is None:
            argument_list = []

        parser = argparse.ArgumentParser()

        for arg in argument_list:
            parser.add_argument("--{0}".format(arg))

        try:
            args, unknown = parser.parse_known_args(argv[1:])
            return vars(args)

        except Exception as e:
            raise Exception("Error parsing input arguments.\n{}".format(e))

    @staticmethod
    def parse_json_file_arg_to_dict(path):
        """
        Tries to parse an XML file into a dictionary.
        :param path: Path to the XML file
        :return: A dictionary. Content is the parsed XML file.
        """
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config_ = json.loads(f.read())
        else:
            raise ImportError("The file %s was not found" % path)
        return config_




