import dlt

# Create empty streaming table

dlt.create_streaming_table(
    name="append_table"
)

#Creating Flow 1
@dlt.append_flow(
    target = 'append_table'
)
def flow_1():
    df = spark.readStream.format("cloudFiles")\
              .option("cloudFiles.format", "csv")\
              .load("/Volumes/databricks_prajakta/bronze/autovol/flow1/")    
        
    return df

#Creating Flow 2
@dlt.append_flow(
    target = 'append_table'
)
def flow_2():
    df = spark.readStream.format("cloudFiles")\
              .option("cloudFiles.format", "csv")\
              .load("/Volumes/databricks_prajakta/bronze/autovol/flow2/")    
        
    return df





