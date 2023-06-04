# models.py

import psycopg2
from datetime import datetime
from psycopg2 import sql

DB_NAME = "Alpha"

# Establish a connection to the database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user="postgres",
    password="Froggykermit8749",
    host="localhost"
)
cur = conn.cursor()

# Create User table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        role_id INTEGER,
        email VARCHAR(255) NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP,
        FOREIGN KEY(role_id) REFERENCES Roles(id)
    )
""")

# Create Roles table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Roles(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE NOT NULL
    )
""")

# Insert roles
roles = ['Admin', 'Manager', 'Assistant Manager', 'Employee']
for role in roles:
    insert = "INSERT INTO Roles (name) VALUES ('{}')".format(role)
    cur.execute(insert)

# Create Categories table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Categories(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE NOT NULL
    )
""")

# Insert categories
categories = ['Pokémon', 'Magic', 'D&D', 'D&D Mini', 'Funko', 'Comics', 'Books', 'Graphic Novels', 'Toys and Figures', 'Sports Cards', 'Posters', 'Dice', 'Board Games', 'Miscellaneous']
for category in categories:
    insert = "INSERT INTO Categories (name) VALUES ('{}')".format(category)
    cur.execute(insert)

# Create Products table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Products(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        category_id INTEGER,
        price DECIMAL(10,2),
        last_order_date TIMESTAMP,
        days_in_stock INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(category_id) REFERENCES Categories(id)
    )
""")

# Create Stock table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Stock(
        id SERIAL PRIMARY KEY,
        product_id INTEGER,
        quantity INTEGER,
        low_stock_threshold INTEGER,
        FOREIGN KEY(product_id) REFERENCES Products(id)
    )
""")

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()
