# inventory.py

import psycopg2

DB_NAME = "Alpha"

# Establish a connection to the database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user="postgres",
    password="Froggykermit8749",
    host="localhost"
)
cur = conn.cursor()

def add_stock(product_id, quantity, low_stock_threshold):
    cur.execute("""
        INSERT INTO Stock(product_id, quantity, low_stock_threshold)
        VALUES (%s, %s, %s)
    """, (product_id, quantity, low_stock_threshold))
    conn.commit()

    print(f"Stock for product id {product_id} added successfully.")

def update_stock(product_id, quantity):
    cur.execute("UPDATE Stock SET quantity = %s WHERE product_id = %s", (quantity, product_id))
    conn.commit()

    print(f"Stock for product id {product_id} updated successfully.")

def check_stock_levels():
    cur.execute("""
        SELECT product_id, quantity 
        FROM Stock 
        WHERE quantity <= low_stock_threshold
    """)
    low_stock_products = cur.fetchall()

    if low_stock_products:
        for product in low_stock_products:
            print(f"Low stock alert for product id {product[0]}. Current quantity: {product[1]}")
    else:
        print("Stock levels are sufficient for all products.")
