from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from l0_bronze_ingest.config.ConfigStore import *
from l0_bronze_ingest.udfs.UDFs import *
from prophecy.utils import *
from l0_bronze_ingest.graph import *

def pipeline(spark: SparkSession) -> None:
    df_L0_raw_shipping = L0_raw_shipping(spark)
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_L0_raw_shipping)
    df_RemoveNullAddr = RemoveNullAddr(spark, df_FlattenSchema_1)
    L1_shipping_delta(spark, df_RemoveNullAddr)
    df_L0_raw_geo_dbfs = L0_raw_geo_dbfs(spark)
    df_RemoveNullZip = RemoveNullZip(spark, df_L0_raw_geo_dbfs)
    df_L0_raw_orders = L0_raw_orders(spark)
    L1_geo_delta(spark, df_RemoveNullZip)
    L1_orders_delta(spark, df_L0_raw_orders)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/L0_bronze_ingest")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/L0_bronze_ingest", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/L0_bronze_ingest")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
