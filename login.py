# login.py

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

def login_user(username):
    cur.execute("""
        SELECT *
        FROM Users
        WHERE username = %s
    """, (username,))
    
    return cur.fetchone()
