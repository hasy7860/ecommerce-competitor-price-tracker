import requests, csv, os, psycopg2
from datetime import datetime

URL = ""

response = requests.get(URL)
data = response.json()

products = data.get("products", [])

rows = []

for product in products:
    product_id = product['id']
    product_title = product['title']

    for variant in product['variants']:
        variant_id = variant["id"]
        sku = variant["sku"]
        price = float(variant["price"])
        compare_at = variant["compare_at_price"]
        available = variant["available"]
        updated_at = variant["updated_at"]
        created_at = variant["created_at"]

    rows.append([product_id, product_title, variant_id, sku, price, compare_at, available, updated_at, created_at, datetime.now()])

file_exists = os.path.isfile("mrbeast_prices.csv")

connect = psycopg2.connect(
    host="localhost",
    dbname="db_name",
    user="user_name",
    password="password",
    port=5432)

cursor = connect.cursor()

insert_query = """INSERT INTO product_price_history (
                  product_id, product_title, variant_id, sku, price,
                  compare_at_price, available, variant_updated_at,
                  variant_created_at, scraped_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

cursor.executemany(insert_query, rows)

connect.commit()
cursor.close()
connect.close()

print("Data inserted successfully.")

#I will continue tomorrow from here :)
