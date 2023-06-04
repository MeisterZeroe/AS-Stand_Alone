# users.py

import psycopg2
from passlib.hash import pbkdf2_sha256

DB_NAME = "Alpha"

# Establish a connection to the database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user="postgres",
    password="Froggykermit8749",
    host="localhost"
)
cur = conn.cursor()

def add_user(username, password, email, role_name):
    hashed_password = pbkdf2_sha256.hash(password)

    conn = None
    try:
        conn = psycopg2.connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT id 
            FROM Roles 
            WHERE name = %s
        """, (role_name,))

        role_id = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO Users (username, password, email, role_id) 
            VALUES (%s, %s, %s, %s)
        """, (username, hashed_password, email, role_id))

        conn.commit()
    finally:
        if conn is not None:
            conn.close()

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
