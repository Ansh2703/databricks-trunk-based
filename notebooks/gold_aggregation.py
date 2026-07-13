# Databricks notebook source
# MAGIC %md
# MAGIC # Gold Layer - Business-Level Aggregations
# MAGIC
# MAGIC This notebook creates analytics-ready tables from silver layer:
# MAGIC - Customer count by state
# MAGIC - Summary statistics
# MAGIC - Business KPIs

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
# MAGIC ## Read from Silver Table

# COMMAND ----------

df_silver = spark.table(f"{catalog}.{schema}.silver_customers")
print(f"Silver records: {df_silver.count()}")
df_silver.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Business Aggregations

# COMMAND ----------

from pyspark.sql.functions import count, current_timestamp

# Aggregate: Customer count by state
df_gold = (
    df_silver.groupBy("state")
    .agg(count("customer_id").alias("customer_count"))
    .withColumn("report_timestamp", current_timestamp())
    .orderBy("customer_count", ascending=False)
)

print(f"Gold aggregated records: {df_gold.count()}")
df_gold.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write to Gold Table

# COMMAND ----------

table_name = f"{catalog}.{schema}.gold_customer_summary"
df_gold.write.mode("overwrite").saveAsTable(table_name)

print(f"✅ Gold table created: {table_name}")
print(f"Records written: {df_gold.count()}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verify Gold Table

# COMMAND ----------

spark.sql(f"""
    SELECT 
        state,
        customer_count,
        report_timestamp
    FROM {catalog}.{schema}.gold_customer_summary
    ORDER BY customer_count DESC
""").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary Statistics

# COMMAND ----------

spark.sql(f"""
    SELECT 
        COUNT(DISTINCT state) as total_states,
        SUM(customer_count) as total_customers,
        AVG(customer_count) as avg_customers_per_state,
        MAX(customer_count) as max_customers_in_state
    FROM {catalog}.{schema}.gold_customer_summary
""").display()
