# user.py

import psycopg2
from passlib.hash import pbkdf2_sha256

def connect():
    return psycopg2.connect(
        host="localhost",
        database="Alpha",
        user="postgres",
        password="Froggykermit8749")

def add_user(username, password, email, role_name):
    hashed_password = pbkdf2_sha256.hash(password)

    conn = None
    try:
        conn = connect()
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
