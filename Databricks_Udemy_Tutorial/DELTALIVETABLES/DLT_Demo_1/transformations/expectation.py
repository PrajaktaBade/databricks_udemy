import dlt

expectations = {
    "rule1 " : "product_id is NOT NULL",
    "rule2" : "category is NOT NULL"
}

# Create streaming table
@dlt.table(
    name = 'expect_table'
)
@dlt.expect_all_or_drop(expectations)
def expect_table():
    df = spark.read.table("databricks_prajakta.silver.products_enr")
    return df
