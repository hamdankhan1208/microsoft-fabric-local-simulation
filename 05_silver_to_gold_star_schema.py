import os
import pandas as pd
from deltalake import DeltaTable, write_deltalake

SILVER_SALES_PATH = "fabric_lakehouse/silver/clean_sales"
GOLD_DIR = "fabric_lakehouse/gold"

print("Reading cleaned data from Silver Layer...")

#Step 1: Loading Silver Data Table
dt_silver = DeltaTable(SILVER_SALES_PATH)
df_silver = dt_silver.to_pandas()
df_silver['timestamp'] = pd.to_datetime(df_silver['timestamp'])

print(f"Loaded {len(df_silver)} rows from Silver.\n")

# Step 2: Build Dimension Tables
print("--- Creating Dimension Tables ---")

#1. Date Dimension(dim_date)
df_silver['date_key'] = df_silver["timestamp"].dt.strftime('%Y%m%d').astype(int)
unique_dates = pd.Series(df_silver['timestamp'].dt.date.unique()).sort_values()

dim_date = pd.DataFrame({'date': pd.to_datetime(unique_dates)})
dim_date['date_key'] = dim_date['date'].dt.strftime('%Y%m%d').astype(int)
dim_date['year'] = dim_date['date'].dt.year
dim_date['month'] = dim_date['date'].dt.month
dim_date['month_name'] = dim_date['date'].dt.strftime('%B')
dim_date['day'] = dim_date['date'].dt.day
dim_date['day_name'] = dim_date['date'].dt.strftime('%A')

#2.Customer Dimension(dim_customer)
dim_customer = df_silver[['customer_id']].drop_duplicates().reset_index(drop=True)
dim_customer['customer_name'] = dim_customer['customer_id'].apply(lambda x: f"Customer Account {x}")

#3.Store Dimension(dim_store)
dim_store = df_silver[['store_id']].drop_duplicates().reset_index(drop=True)
dim_store['store_location'] = dim_store['store_id'].apply(lambda x: f"Retail Outlet {x}")

print("Created dim_date, dim_customer, and dim_store dataframes.")

#Step 3: Building Fact Table
print("\n--- Creating Gold Fact Table ---")

# Fact table keeps metrics and foreign keys referencing dimensions
fact_sales = df_silver[[
    'transaction_id',
    'customer_id',
    'store_id',
    'date_key',
    'amount',
    'timestamp'
]].copy()

print("✅ Created fact_sales dataframe.")

#Step 4: Writing Star Schema to Gold Layer as Delta Tables
tables = {
    "dim_date": dim_date,
    "dim_customer": dim_customer,
    "dim_store": dim_store,
    "fact_sales": fact_sales
}

for name, df in tables.items():
    path = os.path.join(GOLD_DIR, name)
    write_deltalake(path, df, mode="overwrite")
    print(f"Wrote {name} to {path} as Delta Table.")

#Step 5: Verifying Gold Layer Outputs
print("\n--- Gold Layer Summary ---")
for name in tables.keys():
    path = os.path.join(GOLD_DIR, name)
    dt = DeltaTable(path)
    print(f"Table: {name:<12} | Version: {dt.version()} | Rows: {len(dt.to_pandas())}")