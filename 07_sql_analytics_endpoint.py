# 07_sql_analytics_endpoint.py
import duckdb

print("--- SIMULATING FABRIC SQL ANALYTICS ENDPOINT VIA DUCKDB ---")

# DuckDB can directly query local Delta Lake files using SQL
conn = duckdb.connect()
conn.execute("INSTALL delta; LOAD delta;")

# Execute analytical query across Gold Star Schema
query = """
SELECT 
    d.month_name,
    c.customer_name,
    COUNT(f.transaction_id) AS total_orders,
    SUM(f.amount) AS total_revenue
FROM delta_scan('fabric_lakehouse/gold/fact_sales') f
JOIN delta_scan('fabric_lakehouse/gold/dim_date') d ON f.date_key = d.date_key
JOIN delta_scan('fabric_lakehouse/gold/dim_customer') c ON f.customer_id = c.customer_id
GROUP BY d.month_name, c.customer_name
ORDER BY total_revenue DESC;
"""

print(conn.execute(query).df())