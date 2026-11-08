"""Check that each table's expected primary key is really unique."""
import duckdb

con = duckdb.connect("data/olist.duckdb", read_only=True)

# table -> column(s) we expect to uniquely identify each row
EXPECTED_KEYS = {
    "orders": "order_id",
    "customers": "customer_id",
    "products": "product_id",
    "sellers": "seller_id",
    "order_items": "order_id, order_item_id",
    "order_payments": "order_id, payment_sequential",
    "order_reviews": "review_id, order_id",
    "product_category_name_translation": "product_category_name",
}

for table, key in EXPECTED_KEYS.items():
    total, distinct = con.execute(f"""
        SELECT (SELECT COUNT(*) FROM raw.{table}),
               (SELECT COUNT(*) FROM (SELECT DISTINCT {key} FROM raw.{table}))
    """).fetchone()
    status = "OK" if total == distinct else f"NOT UNIQUE ({total - distinct:,} duplicates)"
    print(f"{table:<34} {key:<30} {status}")