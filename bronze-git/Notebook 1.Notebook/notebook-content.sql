-- Fabric notebook source

-- METADATA ********************

-- META {
-- META   "kernel_info": {
-- META     "name": "synapse_pyspark"
-- META   },
-- META   "dependencies": {
-- META     "lakehouse": {
-- META       "default_lakehouse": "0d0eff1a-c9a2-465c-9cda-68f170e346f6",
-- META       "default_lakehouse_name": "input",
-- META       "default_lakehouse_workspace_id": "02388c9c-dc85-46bb-9eaf-4b3762849643",
-- META       "known_lakehouses": [
-- META         {
-- META           "id": "0d0eff1a-c9a2-465c-9cda-68f170e346f6"
-- META         }
-- META       ]
-- META     }
-- META   }
-- META }

-- CELL ********************

-- Welcome to your new notebook
-- Type here in the cell editor to add code!

df = spark.sql("SELECT * FROM input.dbo.a_final_common_table LIMIT 1000")
display(df)

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- MARKDOWN ********************


-- CELL ********************

-- optimize input.dbo.a_final_common_table;
VACUUM input.dbo.a_final_common_table;

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

SELECT count(*) from input.dbo.a_final_common_table

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }
