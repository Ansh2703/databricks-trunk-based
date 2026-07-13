{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "d4dee0b8-6cc7-49d4-ac06-f5bf384ca28d",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "# Gold Layer - Business-Level Aggregations\n",
    "\n",
    "This notebook creates analytics-ready tables from silver layer:\n",
    "- Customer count by state\n",
    "- Summary statistics\n",
    "- Business KPIs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "a70458c8-cb72-4bbf-8285-44b8da1acfa0",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "# Get environment parameters from job parameters or dbutils widgets\n",
    "try:\n",
    "    catalog = dbutils.widgets.get(\"catalog\")\n",
    "    schema = dbutils.widgets.get(\"schema\")\n",
    "except Exception:\n",
    "    # Fallback for local development\n",
    "    catalog = \"gitflow\"\n",
    "    schema = \"gitflow_dev\"\n",
    "\n",
    "print(f\"Target Catalog: {catalog}\")\n",
    "print(f\"Target Schema: {schema}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "b3269aec-794b-40b2-b658-cd927baca397",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Read from Silver Table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "326b98a9-6aae-4c8e-9d82-8f1d40ca4bb3",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_silver = spark.table(f\"{catalog}.{schema}.silver_customers\")\n",
    "print(f\"Silver records: {df_silver.count()}\")\n",
    "df_silver.display()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "1d4fad68-c4c6-4777-b0ec-cac0051efbe9",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Create Business Aggregations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "53bf2243-3b26-454c-b375-2c847ba5d7e2",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.functions import count, current_timestamp\n",
    "\n",
    "# Aggregate: Customer count by state\n",
    "df_gold = (\n",
    "    df_silver.groupBy(\"state\")\n",
    "    .agg(count(\"customer_id\").alias(\"customer_count\"))\n",
    "    .withColumn(\"report_timestamp\", current_timestamp())\n",
    "    .orderBy(\"customer_count\", ascending=False)\n",
    ")\n",
    "\n",
    "print(f\"Gold aggregated records: {df_gold.count()}\")\n",
    "df_gold.display()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "34744384-b063-4f28-a8f1-48c51ade8026",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Write to Gold Table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "4c4e9db0-9985-4112-886b-4a5c106ca77e",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "table_name = f\"{catalog}.{schema}.gold_customer_summary\"\n",
    "df_gold.write.mode(\"overwrite\").saveAsTable(table_name)\n",
    "\n",
    "print(f\"✅ Gold table created: {table_name}\")\n",
    "print(f\"Records written: {df_gold.count()}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "0e03e2a4-a10e-453e-aa8b-fa5e6d7cac0d",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Verify Gold Table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "45bb41da-a4d3-4668-9064-8b101840905a",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "spark.sql(f\"\"\"\n",
    "    SELECT \n",
    "        state,\n",
    "        customer_count,\n",
    "        report_timestamp\n",
    "    FROM {catalog}.{schema}.gold_customer_summary\n",
    "    ORDER BY customer_count DESC\n",
    "\"\"\").display()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "31e73775-4cb2-4d44-8955-97cf8a6b35e6",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Summary Statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "e4cfd7c5-0538-4eff-aad6-88823d167d34",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "spark.sql(f\"\"\"\n",
    "    SELECT \n",
    "        COUNT(DISTINCT state) as total_states,\n",
    "        SUM(customer_count) as total_customers,\n",
    "        AVG(customer_count) as avg_customers_per_state,\n",
    "        MAX(customer_count) as max_customers_in_state\n",
    "    FROM {catalog}.{schema}.gold_customer_summary\n",
    "\"\"\").display()"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": null,
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {},
   "notebookName": "gold_aggregation",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
