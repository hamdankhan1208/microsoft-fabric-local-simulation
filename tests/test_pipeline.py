from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

BRONZE = PROJECT_ROOT / "fabric_lakehouse" / "bronze" / "raw_sales"
SILVER = PROJECT_ROOT / "fabric_lakehouse" / "silver" / "clean_sales"
GOLD = PROJECT_ROOT / "fabric_lakehouse" / "gold"


def test_bronze_table_exists():
    assert BRONZE.exists(), "Bronze table does not exist"


def test_silver_table_exists():
    assert SILVER.exists(), "Silver table does not exist"


def test_gold_tables_exist():
    expected_tables = [
        "dim_customer",
        "dim_date",
        "dim_store",
        "fact_sales",
    ]

    for table in expected_tables:
        assert (GOLD / table).exists(), f"Gold table missing: {table}"


def test_fact_sales_contains_data():
    files = list((GOLD / "fact_sales").glob("*.parquet"))

    assert files, "fact_sales contains no Parquet files"


def test_transaction_ids_are_unique():
    file = list((GOLD / "fact_sales").glob("*.parquet"))[0]
    df = pd.read_parquet(file)

    assert df["transaction_id"].is_unique, "Duplicate transaction IDs found"


def test_sales_amounts_are_positive():
    file = list((GOLD / "fact_sales").glob("*.parquet"))[0]
    df = pd.read_parquet(file)

    assert (df["amount"] > 0).all(), "Non-positive sales amount found"


def test_required_fields_are_not_null():
    file = list((GOLD / "fact_sales").glob("*.parquet"))[0]
    df = pd.read_parquet(file)

    required_columns = [
        "transaction_id",
        "customer_id",
        "store_id",
        "date_key",
        "amount",
        "timestamp",
    ]

    assert not df[required_columns].isnull().any().any(), \
        "Null values found in required fields"