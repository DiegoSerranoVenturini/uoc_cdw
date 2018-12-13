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
