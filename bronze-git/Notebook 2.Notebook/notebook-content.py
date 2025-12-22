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

# Welcome to your new notebook
# Type here in the cell editor to add code!
kaggle_api_token = KGAT_ffa0ef5d0e21aa7dc7c6e36bae499725

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%pip install kaggle --quiet


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import os
import json

kaggle_dir = "/tmp/.kaggle"
os.makedirs(kaggle_dir, exist_ok=True)

kaggle_creds = {
  "username": "vevekk",
  "key": "KGAT_ffa0ef5d0e21aa7dc7c6e36bae499725"
}

with open(f"{kaggle_dir}/kaggle.json", "w") as f:
    json.dump(kaggle_creds, f)

os.chmod(f"{kaggle_dir}/kaggle.json", 0o600)

# Point Kaggle to the config directory
os.environ["KAGGLE_CONFIG_DIR"] = kaggle_dir


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

download_path = "/lakehouse/default/Files/kaggle_data/traffident-change-data"
os.makedirs(download_path, exist_ok=True)

api.dataset_download_files(
    "vcnovb/traffident-change-data",
    path=download_path,
    unzip=True
)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
