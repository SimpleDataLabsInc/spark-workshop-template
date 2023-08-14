from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from l0_bronze_ingest.config.ConfigStore import *
from l0_bronze_ingest.udfs.UDFs import *

def RemoveNullZip(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(col("`customer-address-postcode`").isNotNull())
