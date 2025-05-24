import sqlite3
import json

# Connect to database
conn = sqlite3.connect('mydb.sqlite')
cursor = conn.cursor()

# Fetch product data
cursor.execute("SELECT * FROM Product")
rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]

data = [dict(zip(columns, row)) for row in rows]

# Export to JSON (simulate copy to ADLS)
with open("product_data.json", "w", encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Product data exported to product_data.json")

conn.close()
