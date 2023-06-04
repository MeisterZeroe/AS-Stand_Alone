# auth.py

import psycopg2
import bcrypt

DB_NAME = "Alpha"

# Establish a connection to the database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user="postgres",
    password="Froggykermit8749",
    host="localhost"
)
cur = conn.cursor()

def register_user(username, password, email, role):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cur.execute("""
            INSERT INTO Users(username, password, email, role_id)
            VALUES (%s, %s, %s, 
            (SELECT id FROM Roles WHERE name = %s))
        """, (username, hashed_password, email, role))
        conn.commit()

        print(f"User {username} registered successfully.")
    except psycopg2.errors.UniqueViolation:
        print("Username or email already exists.")
        
def login_user(username, password):
    cur.execute("SELECT password FROM Users WHERE username = %s", (username,))
    db_password = cur.fetchone()

    if db_password is None:
        print("Username does not exist.")
    elif bcrypt.checkpw(password.encode('utf-8'), db_password[0]):
        cur.execute("UPDATE Users SET last_login = CURRENT_TIMESTAMP WHERE username = %s", (username,))
        conn.commit()
        print(f"User {username} logged in successfully.")
    else:
        print("Incorrect password.")
