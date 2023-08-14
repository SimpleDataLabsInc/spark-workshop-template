from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from l0_bronze_ingest.config.ConfigStore import *
from l0_bronze_ingest.udfs.UDFs import *

def L0_raw_orders(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("dbfs:/workshop/data/raw_orders/")
