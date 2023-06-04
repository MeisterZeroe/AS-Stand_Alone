# users.py

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

def add_user(username, hashed_password, role_id):
    cur.execute("""
        INSERT INTO Users (username, password, role_id)
        VALUES (%s, %s, %s)
    """, (username, hashed_password, role_id))
    conn.commit()

def update_user(username, hashed_password, role_id):
    cur.execute("""
        UPDATE Users 
        SET password = %s, role_id = %s
        WHERE username = %s
    """, (hashed_password, role_id, username))
    conn.commit()

def delete_user(username):
    cur.execute("""
        DELETE FROM Users 
        WHERE username = %s
    """, (username,))
    conn.commit()
