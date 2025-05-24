import sqlite3

conn = sqlite3.connect('mydb.sqlite')
cursor = conn.cursor()

dummy_customers = [
    (f'Customer{i}', f'customer{i}@example.com', 'India') for i in range(4, 704)
]

cursor.executemany(
    'INSERT INTO Customer (name, email, country) VALUES (?, ?, ?)',
    dummy_customers
)

conn.commit()
conn.close()

print("✅ Inserted 700 dummy customer records into Customer table.")
