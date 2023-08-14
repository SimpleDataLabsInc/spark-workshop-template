from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from l0_bronze_ingest.config.ConfigStore import *
from l0_bronze_ingest.udfs.UDFs import *

def FlattenSchema_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    flt_col = in0.columns
    selectCols = [col("shippinginfo-address-address1") if "shippinginfo-address-address1" in flt_col else col("shippinginfo.address.address1")\
                    .alias("shippinginfo-address-address1"),                   col("shippinginfo-address-address2") if "shippinginfo-address-address2" in flt_col else col("shippinginfo.address.address2")\
                    .alias("shippinginfo-address-address2"),                   col("shippinginfo-address-city") if "shippinginfo-address-city" in flt_col else col("shippinginfo.address.city")\
                    .alias("shippinginfo-address-city"),                   col("shippinginfo-address-country") if "shippinginfo-address-country" in flt_col else col("shippinginfo.address.country")\
                    .alias("shippinginfo-address-country"),                   col("shippinginfo-address-postcode") if "shippinginfo-address-postcode" in flt_col else col("shippinginfo.address.postcode")\
                    .alias("shippinginfo-address-postcode"),                   col("shippinginfo-address-state") if "shippinginfo-address-state" in flt_col else col("shippinginfo.address.state")\
                    .alias("shippinginfo-address-state"),                   col("shippinginfo-method") if "shippinginfo-method" in flt_col else col("shippinginfo.method")\
                    .alias("shippinginfo-method"),                   col("shippinginfo-recipient-firstname") if "shippinginfo-recipient-firstname" in flt_col else col("shippinginfo.recipient.firstname")\
                    .alias("shippinginfo-recipient-firstname"),                   col("shippinginfo-recipient-lastname") if "shippinginfo-recipient-lastname" in flt_col else col("shippinginfo.recipient.lastname")\
                    .alias("shippinginfo-recipient-lastname"),                   col("email") if "email" in flt_col else col("email")]

    return in0.select(*selectCols)
