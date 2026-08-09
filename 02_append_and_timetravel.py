import pandas as pd
from deltalake import write_deltalake, DeltaTable

BRONZE_SALES_PATH = "fabric_lakehouse/bronze/raw_sales"

#Step 1: Preparing a second batch of transactions (Day 2 data)
new_sales_data = pd.DataFrame({
    "transaction_id": [1004, 1005],
    "customer_id": ["C104", "C101"],
    "amount": [310.00, 45.00],
    "store_id": ["S01", "S02"],
    "timestamp": ["2026-08-02 08:30:00", "2026-08-02 09:15:00"]
})

print("🚀 Appending new transactions (Batch 2) to Bronze...")

# Mode 'append' adds new records without overwriting existing data
write_deltalake(BRONZE_SALES_PATH, new_sales_data, mode="append")

print("✅ Appended batch successfully!\n")

#Step 2: Read the latest state of the table
dt_latest = DeltaTable(BRONZE_SALES_PATH)
current_ver = dt_latest.version()
print(f"Current Delta Table Version: {current_ver}")

print(f"\n--- Current Data (Version {current_ver} - Total {len(dt_latest.to_pandas())} rows) ---")
print(dt_latest.to_pandas())

#Step 3: TIME TRAVEL - Load Historical snapshot (Version 1)
print("\n--- TIME TRAVEL DEMO: Reading Version 1 Snapshot ---")
dt_v1 = DeltaTable(BRONZE_SALES_PATH, version=1)
df_v1 = dt_v1.to_pandas()
print(f"Version 1 Record Count: {len(df_v1)} rows")
print(df_v1)