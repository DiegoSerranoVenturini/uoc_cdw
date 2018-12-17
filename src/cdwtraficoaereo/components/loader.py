import abc
from pyspark.sql import SparkSession

from cdwtraficoaereo.fw import DataLoader


class UniversalDataLoader(DataLoader):

    def load_data(self, *args, **kwargs):

        raw_data = self._load_data(*args, **kwargs)

        raw_data = self.rename_columns(raw_data, **kwargs)

        return raw_data

    @abc.abstractmethod
    def _load_data(self, *args, **kwargs):
        pass

    @staticmethod
    def rename_columns(raw_data, **kwargs):
        if "colnames" not in kwargs.keys():
            return raw_data

        colnames = kwargs["colnames"]
        if isinstance(colnames, list) and colnames is not None and len(colnames) == len(raw_data.columns):
            for idx, c in enumerate(raw_data.columns):
                raw_data = raw_data.withColumnRenamed(c, colnames[idx])

        return raw_data


class CsvDataLoader(UniversalDataLoader):

    def _load_data(self, spark: SparkSession, path: str, header=True, infer_schema=True, colnames=None, **kwargs):

        raw_data = spark.read.option("header", header).option("inferSchema", infer_schema).csv(path)

        return raw_data


class JsonDataLoader(UniversalDataLoader):

    def _load_data(self, spark: SparkSession, path: str, header=True, infer_schema=True, sep=",", encoding="latin1", colnames=None, **kwargs):

        raw_data = spark.read.json(path)

        return raw_data


class XmlDataLoader(UniversalDataLoader):

    def _load_data(self, spark: SparkSession, path: str, header=True, infer_schema=True, sep=",", encoding="latin1", row_tag="row", colnames=None, **kwargs):

        raw_data = spark.read.format("com.databricks.spark.xml").load(path, rowTag=row_tag)

        return raw_data
