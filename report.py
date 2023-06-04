# report.py

import psycopg2
import fpdf

DB_NAME = "alphashot_inventory"

# Establish a connection to the database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user="your_user",
    password="your_password",
    host="localhost"
)
cur = conn.cursor()

def generate_sales_report():
    cur.execute("""
        SELECT Sales.product_id, Products.name, SUM(Sales.quantity) as total_sold, SUM(Sales.total_price) as total_revenue
        FROM Sales
        JOIN Products ON Sales.product_id = Products.id
        GROUP BY Sales.product_id, Products.name
    """)
    sales_data = cur.fetchall()

    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')

    # Column headers
    pdf.cell(50, 10, txt="Product ID", border=1)
    pdf.cell(50, 10, txt="Product Name", border=1)
    pdf.cell(50, 10, txt="Total Sold", border=1)
    pdf.cell(50, 10, txt="Total Revenue", border=1, ln=True)

    # Data
    for row in sales_data:
        pdf.cell(50, 10, txt=str(row[0]), border=1)
        pdf.cell(50, 10, txt=str(row[1]), border=1)
        pdf.cell(50, 10, txt=str(row[2]), border=1)
        pdf.cell(50, 10, txt=str(row[3]), border=1, ln=True)

    pdf.output("sales_report.pdf")

    print("Sales report generated successfully.")
