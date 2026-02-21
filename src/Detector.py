def detect_price_drops(connect):
    cursor = connect.cursor()

    query = """WITH ranked AS (SELECT variant_id, product_title,
               price, scraped_at, ROW_NUMBER() OVER (
               PARTITION BY variant_id
               ORDER BY scraped_at DESC) as rn
               FROM product_price_history),
               latest AS (SELECT * FROM ranked WHERE rn = 1),
               previous AS (SELECT * FROM ranked WHERE rn = 2)

               SELECT
                l.variant_id,
                l.product_title,
                p.price AS old_price,
                l.price AS new_price
                FROM latest l
                JOIN previous p
                    ON l.variant_id = p.variant_id
                WHERE l.price < p.price;"""

    cursor.execute(query)
    drops = cursor.fetchall()

    cursor.close()
    return drops
