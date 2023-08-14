from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from l0_bronze_ingest.config.ConfigStore import *
from l0_bronze_ingest.udfs.UDFs import *

def L0_raw_geo_dbfs(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("customer-address-city", StringType(), True), StructField("customer-address-country", StringType(), True), StructField("customer-address-postcode", IntegerType(), True), StructField("customer-address-state", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/workshop/data/raw_geo/")
