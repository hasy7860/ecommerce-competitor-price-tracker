from datetime import datetime

def transformer(data):
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
    return rows
