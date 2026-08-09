from pathlib import Path


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