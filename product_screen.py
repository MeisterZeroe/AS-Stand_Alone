# product_screen.py

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from product import add_product, fetch_categories, search_product


class ProductScreen:
    def __init__(self, root):
        self.root = root
        self.root.title('Product Management')
        
        # Adding product name entry
        self.product_name_label = ttk.Label(root, text='Product Name:')
        self.product_name_label.grid(row=0, column=0)
        
        self.product_name_entry = ttk.Entry(root)
        self.product_name_entry.grid(row=0, column=1)
        
        # Adding product category entry
        self.product_category_label = ttk.Label(root, text='Product Category:')
        self.product_category_label.grid(row=1, column=0)
        
        self.product_category = ttk.Combobox(root, values=fetch_categories())
        self.product_category.grid(row=1, column=1)
        
        # Adding product price entry
        self.product_price_label = ttk.Label(root, text='Product Price:')
        self.product_price_label.grid(row=2, column=0)
        
        self.product_price_entry = ttk.Entry(root)
        self.product_price_entry.grid(row=2, column=1)
        
        # Adding product add button
        self.add_product_button = ttk.Button(root, text='Add Product', command=self.add_product)
        self.add_product_button.grid(row=3, column=0, columnspan=2)

    def add_product(self):
        name = self.product_name_entry.get()
        category = self.product_category.get()
        price = float(self.product_price_entry.get())  # Convert the price to float

        add_product(name, category, price, None, 0, 0)  # Other fields are set to default values

        self.product_name_entry.delete(0, tk.END)
        self.product_category.set('')  # Clear the selected category
        self.product_price_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    ps = ProductScreen(root)
    root.mainloop()
