# Databricks notebook source
# MAGIC %md
# MAGIC # Silver Layer - Data Cleansing and Transformation
# MAGIC
# MAGIC This notebook reads from bronze table and applies:
# MAGIC - Data quality checks (remove nulls)
# MAGIC - Standardization (trim whitespace, uppercase state codes)
# MAGIC - Add business metadata

# COMMAND ----------

# Get environment parameters from job parameters or dbutils widgets
try:
    catalog = dbutils.widgets.get("catalog")
    schema = dbutils.widgets.get("schema")
except Exception:
    # Fallback for local development
    catalog = "gitflow"
    schema = "gitflow_dev"

print(f"Target Catalog: {catalog}")
print(f"Target Schema: {schema}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Read from Bronze Table

# COMMAND ----------

df_bronze = spark.table(f"{catalog}.{schema}.bronze_customers")
print(f"Bronze records: {df_bronze.count()}")
df_bronze.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Apply Data Quality Rules

# COMMAND ----------

from pyspark.sql.functions import col, trim, upper, current_timestamp, current_date

# Data quality transformations
df_silver = (
    df_bronze.filter(col("customer_id").isNotNull())
    .filter(col("customer_name").isNotNull())
    .withColumn("customer_name", trim(col("customer_name")))
    .withColumn("state", upper(trim(col("state"))))
    .withColumn("processed_timestamp", current_timestamp())
    .withColumn("processing_date", current_date())
)

print(f"Silver records after quality checks: {df_silver.count()}")
df_silver.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write to Silver Table

# COMMAND ----------

table_name = f"{catalog}.{schema}.silver_customers"
df_silver.write.mode("overwrite").saveAsTable(table_name)

print(f"✅ Silver table created: {table_name}")
print(f"Records written: {df_silver.count()}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verify Silver Table

# COMMAND ----------

spark.sql(f"SELECT * FROM {catalog}.{schema}.silver_customers LIMIT 10").display()
