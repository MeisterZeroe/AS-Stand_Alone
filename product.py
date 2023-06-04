# product.py

import psycopg2
from datetime import datetime

DB_NAME = "Alpha"

# Establish a connection to the database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user="postgres",
    password="Froggykermit8749",
    host="localhost"
)
cur = conn.cursor()

def add_product(name, category, price):
    cur.execute("""
        INSERT INTO Products(name, category_id, price, created_at)
        VALUES (%s, 
        (SELECT id FROM Categories WHERE name = %s),
        %s, %s)
    """, (name, category, price, datetime.now()))
    conn.commit()

    print(f"Product {name} added successfully.")

def search_product(search_term):
    # Search by product name
    cur.execute("SELECT * FROM Products WHERE name LIKE %s", ('%' + search_term + '%',))
    products = cur.fetchall()

    if not products:
        # Search by category name
        cur.execute("""
            SELECT * FROM Products 
            WHERE category_id = 
            (SELECT id FROM Categories WHERE name LIKE %s)
        """, ('%' + search_term + '%',))
        products = cur.fetchall()

    if products:
        for product in products:
            print(product)
    else:
        print("No products found.")

def fetch_categories():
    cur.execute("""
        SELECT name 
        FROM Categories
    """)
    
    return [row[0] for row in cur.fetchall()]
