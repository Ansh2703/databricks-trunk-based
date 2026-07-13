{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "3f639450-89a1-4385-8aaf-0a4ad73e9d6d",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "# Silver Layer - Data Cleansing and Transformation\n",
    "\n",
    "This notebook reads from bronze table and applies:\n",
    "- Data quality checks (remove nulls)\n",
    "- Standardization (trim whitespace, uppercase state codes)\n",
    "- Add business metadata"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "e04e9d35-d3cd-4af9-a19a-075697af53a3",
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
     "nuid": "6f8da45f-a982-42de-8456-d9177654978f",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Read from Bronze Table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "64e09d69-100a-4a5a-a4aa-3b30f05204c8",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_bronze = spark.table(f\"{catalog}.{schema}.bronze_customers\")\n",
    "print(f\"Bronze records: {df_bronze.count()}\")\n",
    "df_bronze.display()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "6d8b9e4c-05da-4b80-abda-39b9e1f96993",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Apply Data Quality Rules"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "2536c821-db1b-43c4-ae7e-e88a33e525c7",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.functions import col, trim, upper, current_timestamp, current_date\n",
    "\n",
    "# Data quality transformations\n",
    "df_silver = (\n",
    "    df_bronze.filter(col(\"customer_id\").isNotNull())\n",
    "    .filter(col(\"customer_name\").isNotNull())\n",
    "    .withColumn(\"customer_name\", trim(col(\"customer_name\")))\n",
    "    .withColumn(\"state\", upper(trim(col(\"state\"))))\n",
    "    .withColumn(\"processed_timestamp\", current_timestamp())\n",
    "    .withColumn(\"processing_date\", current_date())\n",
    ")\n",
    "\n",
    "print(f\"Silver records after quality checks: {df_silver.count()}\")\n",
    "df_silver.display()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "928def25-cc96-47b7-9fd1-dcd22a6a2bb4",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Write to Silver Table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "6443d5d5-16ec-4de7-8730-842cc30fb89a",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "table_name = f\"{catalog}.{schema}.silver_customers\"\n",
    "df_silver.write.mode(\"overwrite\").saveAsTable(table_name)\n",
    "\n",
    "print(f\"✅ Silver table created: {table_name}\")\n",
    "print(f\"Records written: {df_silver.count()}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "e7fd9183-3e6c-4c42-a9fc-441ae59bda90",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Verify Silver Table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "13247709-929d-4b54-891f-a30b17a8eabf",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "spark.sql(f\"SELECT * FROM {catalog}.{schema}.silver_customers LIMIT 10\").display()"
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
   "notebookName": "silver_transformation",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
