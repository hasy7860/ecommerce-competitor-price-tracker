import requests, os, psycopg2, yagmail
from src.transformer import transformer
from src.reporter import send_alert
from src.Detector import detect_price_drops

URL = "https://mrbeast.store/products.json"

#Extract
response = requests.get(URL)
data = response.json()

#Transform
transformed_data = transformer(data)

#Load
connect = psycopg2.connect(
        host="localhost",
        dbname="ecommerce_competitor_price_tracker",
        user="postgres",
        password="1234",
        port=5432)

cursor = connect.cursor()

insert_query = """INSERT INTO product_price_history (
                  product_id, product_title, variant_id, sku, price,
                  compare_at_price, available, variant_updated_at,
                  variant_created_at, scraped_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

cursor.executemany(insert_query, transformed_data)
connect.commit()

#Detect
drops = detect_price_drops(connect)

#Report
if drops:
    send_alert(drops)

cursor.close()
connect.close()