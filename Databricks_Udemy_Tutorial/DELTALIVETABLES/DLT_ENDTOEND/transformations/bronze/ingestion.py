import dlt

#Ingesting Sales data
@dlt.table(
    name = 'sales_bronze'
)

def sales_bronze():
    df = spark.readStream.format('CloudFiles')\
              .option("cloudFiles.format", "csv")\
              .load("/Volumes/databricks_prajakta/bronze/bronze_volume/sales/")
    return df

#Ingesting Stores data
@dlt.table(
    name = 'stores_bronze'
)

def stores_bronze():
    df = spark.readStream.format('CloudFiles')\
              .option("cloudFiles.format", "csv")\
              .load("/Volumes/databricks_prajakta/bronze/bronze_volume/stores/")
    return df

#Ingesting Customers data
@dlt.table(
    name = 'customers_bronze'
)

def customers_bronze():
    df = spark.readStream.format('CloudFiles')\
              .option("cloudFiles.format", "csv")\
              .load("/Volumes/databricks_prajakta/bronze/bronze_volume/customers/")
    return df

#Ingesting Products data
@dlt.table(
    name = 'products_bronze'
)

def products_bronze():
    df = spark.readStream.format('CloudFiles')\
              .option("cloudFiles.format", "csv")\
              .load("/Volumes/databricks_prajakta/bronze/bronze_volume/products/")
    return df