import sqlite3
import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime

print("Step 1: Libraries import ho gayi hain.")

# Step 2: Fake Data Generate Karna
fake = Faker('en_IN')

# Data generation
employees_data = [(i, fake.name()) for i in range(1, 101)]
stores_data = [(1, 'Delhi'), (2, 'Mumbai'), (3, 'Bangalore'), (4, 'Varanasi')]
products_data = [
    (101, 'Laptop', 'Electronics', 50000, 65000),
    (102, 'Mouse', 'Electronics', 800, 1200),
    (103, 'T-Shirt', 'Apparel', 500, 900),
    (104, 'Jeans', 'Apparel', 1500, 2500),
    (105, 'Shampoo', 'FMCG', 300, 450)
]

sales_data = []
for i in range(1, 5001):
    sale_id = i
    product_id = random.choice([101, 102, 103, 104, 105])
    employee_id = random.randint(1, 100)
    store_id = random.randint(1, 4)
    quantity = random.randint(1, 5)
    sales_data.append((sale_id, product_id, employee_id, store_id, quantity))

print(f"Step 2: {len(employees_data)} employees, {len(stores_data)} stores, aur {len(sales_data)} sales ka fake data taiyar hai.")

# Step 3: Database Banana aur Data Daalna (SQL ka Kaam)
conn = sqlite3.connect('retail_db.db')
cursor = conn.cursor()

# Purani tables delete karna
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS stores")
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS sales")

# Tables banana
cursor.execute("CREATE TABLE employees (employee_id INTEGER, name TEXT)")
cursor.execute("CREATE TABLE stores (store_id INTEGER, location TEXT)")
cursor.execute("CREATE TABLE products (product_id INTEGER, product_name TEXT, category TEXT, cost_price REAL, selling_price REAL)")
cursor.execute("CREATE TABLE sales (sale_id INTEGER, product_id INTEGER, employee_id INTEGER, store_id INTEGER, quantity INTEGER)")

# Data daalna
cursor.executemany("INSERT INTO employees VALUES (?, ?)", employees_data)
cursor.executemany("INSERT INTO stores VALUES (?, ?)", stores_data)
cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?)", products_data)
cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?)", sales_data)

conn.commit()
print("Step 3: Database mein data daal diya gaya hai.")

# Step 4: Complex JOIN se Data Nikalna (SQL ka Kaam)
sql_query = """
SELECT
    s.sale_id,
    e.name AS employee_name,
    st.location,
    p.product_name,
    p.category,
    p.cost_price,
    p.selling_price,
    s.quantity
FROM sales s
JOIN employees e ON s.employee_id = e.employee_id
JOIN stores st ON s.store_id = st.store_id
JOIN products p ON s.product_id = p.product_id;
"""
df = pd.read_sql_query(sql_query, conn)
conn.close()
print("Step 4: SQL se 4 tables ko JOIN karke data DataFrame mein aa gaya hai.")

# Step 5: Analysis aur Feature Engineering (Pandas ka Kaam)
df['revenue'] = df['selling_price'] * df['quantity']
df['profit'] = (df['selling_price'] - df['cost_price']) * df['quantity']
print("Step 5: 'Revenue' aur 'Profit' columns ban gaye hain.")

# Step 6: Alag-alag Reports Banana (Pandas ka Kaam)
employee_performance = df.groupby('employee_name').agg(total_revenue=('revenue', 'sum'), total_profit=('profit', 'sum')).reset_index()
store_performance = df.groupby('location').agg(total_revenue=('revenue', 'sum'), total_profit=('profit', 'sum')).reset_index()
product_performance = df.groupby(['category', 'product_name']).agg(units_sold=('quantity', 'sum'), total_revenue=('revenue', 'sum'), total_profit=('profit', 'sum')).reset_index()
print("Step 6: Employee, Store, aur Product ke liye summary reports taiyar hain.")

# Step 7: Employee Tier Banana (NumPy ka Kaam)
conditions = [
    (employee_performance['total_revenue'] >= 200000),
    (employee_performance['total_revenue'] >= 100000)
]
choices = ['Gold Tier', 'Silver Tier']
employee_performance['tier'] = np.select(conditions, choices, default='Bronze Tier')
print("Step 7: Employee performance tier ban gaya hai.")

# Step 8: Power BI ke Liye Files Taiyar Karna
employee_performance.to_csv('employee_report.csv', index=False)
store_performance.to_csv('store_report.csv', index=False)
product_performance.to_csv('product_report.csv', index=False)

print("\n--- Project Poora Hua ---")
print("Power BI ke liye 3 CSV files (employee, store, product reports) aapke folder mein taiyar hain.")