{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "a335beb0-59ad-487e-9cbc-4d8ff9b0f8bc",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "# Bronze Layer - Raw Data Ingestion\n",
    "\n",
    "This notebook ingests raw customer data from Databricks sample datasets.\n",
    "No transformations - just load raw data into bronze table."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "c7bfa129-3915-4ffb-ab64-3ecca082ef8c",
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
     "nuid": "c90e4354-83fe-4ee6-a55f-4547119e9742",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Read Raw Data from Databricks Sample Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "4d456789-dec8-4da9-babf-58d5dbcefc2d",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "# Read sample customer data\n",
    "df_raw = spark.read.csv(\n",
    "    \"/databricks-datasets/retail-org/customers/\", header=True, inferSchema=True\n",
    ")\n",
    "\n",
    "print(f\"Records read: {df_raw.count()}\")\n",
    "df_raw.display()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "8cd663d8-4758-4f4c-ad69-18219554fdfe",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Write to Bronze Table (No Transformations)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "b3e5433f-45e4-40ce-a2cb-ff37023d877a",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.functions import current_timestamp\n",
    "\n",
    "# Add metadata columns\n",
    "df_bronze = df_raw.withColumn(\"ingestion_timestamp\", current_timestamp())\n",
    "\n",
    "# Write to bronze table\n",
    "table_name = f\"{catalog}.{schema}.bronze_customers\"\n",
    "df_bronze.write.mode(\"overwrite\").saveAsTable(table_name)\n",
    "\n",
    "print(f\"✅ Bronze table created: {table_name}\")\n",
    "print(f\"Records written: {df_bronze.count()}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "ea06e0b1-4877-440b-912c-001a9c57d19f",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Verify Bronze Table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "d43edf27-016e-4d25-bf67-4c42008dc541",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "spark.sql(f\"SELECT * FROM {catalog}.{schema}.bronze_customers LIMIT 10\").display()"
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
   "notebookMetadata": {
    "pythonIndentUnit": 4
   },
   "notebookName": "bronze_ingestion",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
