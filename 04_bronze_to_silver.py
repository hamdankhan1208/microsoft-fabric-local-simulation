import pandas as pd
from deltalake import DeltaTable, write_deltalake

BRONZE_SALES_PATH = "fabric_lakehouse/bronze/raw_sales"
SILVER_SALES_PATH = "fabric_lakehouse/silver/clean_sales"

print("Reading raw data from Bronze layer...")

#Step 1: Reading the latest Delta table from Bronze
dt_bronze = DeltaTable(BRONZE_SALES_PATH)
df_raw = dt_bronze.to_pandas()

print(f"Loaded {len(df_raw)} rows from Bronze.")
print(df_raw)

print("\n--- Applying Silver Layer Data Cleaning ---")

#Step 2: Data Cleaning and Transformation Operations
#1. Deduplication: Removing any duplicate rows based on transaction_id
df_clean = df_raw.drop_duplicates(subset=["transaction_id"])

#2. Schema Enforcement / Data Type Casting: Ensuring correct types
df_clean["transaction_id"] = df_clean["transaction_id"].astype(int)
df_clean["amount"] = df_clean["amount"].astype(float)
df_clean["timestamp"] = pd.to_datetime(df_clean["timestamp"])

#3. Data Hygiene Filter: Removing rows where amount is zero or negative
df_clean = df_clean[df_clean["amount"] > 0]

print(f"Cleaned data has {len(df_clean)} rows remaining after filtering.")

#Step 3: Writing cleaned data to the Silver Layer as a Delta Table
write_deltalake(SILVER_SALES_PATH, df_clean, mode="overwrite")

print("\nSuccessfully wrote clean data to Silver layer!")

#Step 4: Verify the Silver Delta Table
dt_silver = DeltaTable(SILVER_SALES_PATH)
print(f"Silver Delta Table Version: {dt_silver.version()}")
print(dt_silver.to_pandas())