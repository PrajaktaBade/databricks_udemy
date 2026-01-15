import dlt
from pyspark.sql.functions import * 

# Create Streaming table(Using Autoloader)
@dlt.table(
  name="autovol_table"
)
def autovol():
  df = spark.readStream.format("cloudFiles")\
            .option("cloudFiles.format", "csv")\
            .load("/Volumes/databricks_prajakta/bronze/autovol/raw/")
  return df
       
#Creating Streaming table 
@dlt.table(
  name="autovol_table_enr"
)
def autovol_table_enr():
  df = spark.read.table("autovol_table")
  df = df.withColumn("flag",lit("Yes"))

  return df
                     







