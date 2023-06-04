# main.py

import tkinter as tk
from tkinter import messagebox
import bcrypt
import psycopg2

from login import login_user
from users import add_user, update_user, delete_user
from product import add_product, search_product

DB_NAME = "Alpha"

# Establish a connection to the database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user="postgres",
    password="Froggykermit8749",
    host="localhost"
)
cur = conn.cursor()

# Root window
root = tk.Tk()
root.title("Alphashot Inventory")
root.geometry("800x600")

# Frame for login
frame_login = tk.Frame(root)
frame_login.place(relx=0.5, rely=0.5, anchor="center")

label_username = tk.Label(frame_login, text="Username")
label_password = tk.Label(frame_login, text="Password")

entry_username = tk.Entry(frame_login)
entry_password = tk.Entry(frame_login, show="*")

label_username.grid(row=0, column=0)
entry_username.grid(row=0, column=1)
label_password.grid(row=1, column=0)
entry_password.grid(row=1, column=1)

def login():
    username = entry_username.get()
    password = entry_password.get().encode('utf-8')

    user = login_user(username)

    if user and bcrypt.checkpw(password, user[2].encode('utf-8')):
        messagebox.showinfo("Login success", "Welcome " + user[1])
        # TODO: Navigate to dashboard
    else:
        messagebox.showerror("Login failed", "Invalid username or password")

button_login = tk.Button(frame_login, text="Login", command=login)
button_login.grid(row=2, columnspan=2)

root.mainloop()
