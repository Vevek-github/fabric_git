# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "0d0eff1a-c9a2-465c-9cda-68f170e346f6",
# META       "default_lakehouse_name": "input",
# META       "default_lakehouse_workspace_id": "02388c9c-dc85-46bb-9eaf-4b3762849643",
# META       "known_lakehouses": [
# META         {
# META           "id": "0d0eff1a-c9a2-465c-9cda-68f170e346f6"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

import pandas as pd

wrangler_sample_df = pd.read_csv("abfss://bronze_workspace@onelake.dfs.fabric.microsoft.com/input.Lakehouse/Files/kaggle_data/winemag-data-130k-v2.csv")
display(wrangler_sample_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "editable": true
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

df = spark.read.format("csv").option("header","true").load("abfss://bronze_workspace@onelake.dfs.fabric.microsoft.com/input.Lakehouse/Files/kaggle_data/winemag-data_first150k.csv")
# df now is a Spark DataFrame containing CSV data from "abfss://bronze_workspace@onelake.dfs.fabric.microsoft.com/input.Lakehouse/Files/kaggle_data/winemag-data_first150k.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
