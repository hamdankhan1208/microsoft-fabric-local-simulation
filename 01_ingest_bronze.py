import os
import pandas as pd
from deltalake import write_deltalake, DeltaTable

#Define path for our Bronze table
BRONZE_SALES_PATH = "fabric_lakehouse/bronze/raw_sales"

#Step 1: Creating a batch of raw incoming sales data
raw_sales_data = pd.DataFrame({
    "transaction_id": [1001, 1002, 1003],
    "customer_id": ["C101", "C102", "C103"],
    "amount": [250.00, 120.00, 75.25],
    "store_id": ["S01", "S02", "S03"],
    "timestamp": ["2026-08-01 09:15:00", "2026-08-01 10:30:00", "2026-08-01 11:45:00"]
})

print("🚀 Ingesting raw data into Bronze layer...")

#Step 2: Writing data as a Delta Table (Version 0)
write_deltalake(BRONZE_SALES_PATH, raw_sales_data, mode="overwrite")

print("✅ Data written to Bronze successfully!\n")

#Step 3: Read back the metadata to inspect what Delta created
dt = DeltaTable(BRONZE_SALES_PATH)

print(f"Current Delta Table Version: {dt.version()}")
print(f"Underlying Parquet Files: {dt.file_uris()}")

print("\n--- Current Bronze Data ---")
print(dt.to_pandas())