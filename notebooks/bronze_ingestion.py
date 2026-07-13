# Databricks notebook source
# MAGIC %md
# MAGIC # Bronze Layer - Raw Data Ingestion
# MAGIC
# MAGIC This notebook ingests raw customer data from Databricks sample datasets.
# MAGIC No transformations - just load raw data into bronze table.

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
# MAGIC ## Read Raw Data from Databricks Sample Dataset

# COMMAND ----------

# Read sample customer data
df_raw = spark.read.csv(
    "/databricks-datasets/retail-org/customers/", header=True, inferSchema=True
)

print(f"Records read: {df_raw.count()}")
df_raw.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write to Bronze Table (No Transformations)

# COMMAND ----------

from pyspark.sql.functions import current_timestamp

# Add metadata columns
df_bronze = df_raw.withColumn("ingestion_timestamp", current_timestamp())

# Write to bronze table
table_name = f"{catalog}.{schema}.bronze_customers"
df_bronze.write.mode("overwrite").saveAsTable(table_name)

print(f"✅ Bronze table created: {table_name}")
print(f"Records written: {df_bronze.count()}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verify Bronze Table

# COMMAND ----------

spark.sql(f"SELECT * FROM {catalog}.{schema}.bronze_customers LIMIT 10").display()
