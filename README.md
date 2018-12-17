#UOC - CDW

Source code developed to complete the use cases proposed in the Construction of the Data Warehouse 
subject from the Data Science Master in the UOC.

## Package `cdwtraficoaereo`

The library contains some utilities for building a simple ETL pipeline to load, process and merge the data sources provided in the 
practical use cases.

It accepts a command line argument: `sources` indicating the path to the configuration file with the source definition.

After loading the raw data sources with spark it processes the sources and builds with joins and some
`pyspark.sql` transformations the final expected DWH's tables.

