from deltalake import DeltaTable

BRONZE_SALES_PATH = "fabric_lakehouse/bronze/raw_sales"

#Step 1: Inspecting the table state before optimization
dt = DeltaTable(BRONZE_SALES_PATH)

print("--- 1. BEFORE OPTIMIZATION ---")
files_before = dt.file_uris()
print(f"Active Parquet Files count: {len(files_before)}")
for file in files_before:
    print(f"  └─ {file.split('/')[-1]}")

#Step 2: Running Compaction(Optimize)
print("\n--- 2. RUNNING COMPACTION (OPTIMIZE) ---")
#Compactor merges small files into fewer large files
metrics = dt.optimize.compact()
print("Compaction Complete!")

#Refreshing DeltaTable instance to read new commit
dt = DeltaTable(BRONZE_SALES_PATH)
files_after_compact = dt.file_uris()
print(f"\nActive Parquet files count after compaction: {len(files_after_compact)}")
for file in files_after_compact:
    print(f"  └─ {file.split('/')[-1]}")

#Step 3: Running VACUUM to clean up obselete files
print("\n--- 3. RUNNING VACUUM ---")
#retention_hours=0 and enforce_retention_duration=false allows immediate cleanup for demonstration purposes
deleted_files = dt.vacuum(retention_hours=0, enforce_retention_duration=False, dry_run=False)

print(f"Deleted {len(deleted_files)} obsolete physical files from disk.")

# Final Inspection
dt = DeltaTable(BRONZE_SALES_PATH)
print(f"\nFinal Active Parquet files count: {len(dt.file_uris())}")