from abc import ABC, abstractmethod


class PipelineRunner(ABC):

    @abstractmethod
    def run_etl_pipeline(self, *args, **kwargs):
        pass


class DataLoader(ABC):

    @abstractmethod
    def load_data(self, *args, **kwargs):
        pass


class Factory(ABC):

    @staticmethod
    @abstractmethod
    def build():
        pass


class SourceProcessor(ABC):

    SOURCE = None

    def set_source(self, source):
        self.SOURCE = source

    @property
    def source(self):
        return self.SOURCE

    @abstractmethod
    def process(self, raw_df, *args):
        pass
