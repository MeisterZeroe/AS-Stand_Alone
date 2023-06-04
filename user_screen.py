# user_screen.py

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from users import add_user

class UserScreen:
    def __init__(self, root):
        self.root = root
        self.root.title('User Management')

        # Adding username entry
        self.username_label = ttk.Label(root, text='Username:')
        self.username_label.grid(row=0, column=0)
        
        self.username_entry = ttk.Entry(root)
        self.username_entry.grid(row=0, column=1)
        
        # Adding password entry
        self.password_label = ttk.Label(root, text='Password:')
        self.password_label.grid(row=1, column=0)
        
        self.password_entry = ttk.Entry(root, show='*')  # The password will be hidden
        self.password_entry.grid(row=1, column=1)
        
        # Adding email entry
        self.email_label = ttk.Label(root, text='Email:')
        self.email_label.grid(row=2, column=0)
        
        self.email_entry = ttk.Entry(root)
        self.email_entry.grid(row=2, column=1)
        
        # Adding role entry
        self.role_label = ttk.Label(root, text='Role:')
        self.role_label.grid(row=3, column=0)
        
        self.role_entry = ttk.Entry(root)
        self.role_entry.grid(row=3, column=1)
        
        # Adding add user button
        self.add_user_button = ttk.Button(root, text='Add User', command=self.add_user)
        self.add_user_button.grid(row=4, column=0, columnspan=2)

    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        role = self.role_entry.get()

        add_user(username, password, email, role)

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.role_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    us = UserScreen(root)
    root.mainloop()
