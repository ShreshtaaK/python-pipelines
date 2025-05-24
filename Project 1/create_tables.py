import sqlite3

conn = sqlite3.connect('mydb.sqlite')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        country TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        price REAL NOT NULL
    )
''')

customers = [
    ('John Doe', 'john@example.com', 'India'),
    ('Jane Smith', 'jane@example.com', 'US'),
    ('Alice Johnson', 'alice@example.com', 'UK')
]

cursor.executemany('INSERT INTO Customer (name, email, country) VALUES (?, ?, ?)', customers)

conn.commit()
conn.close()

print("Tables created and sample data inserted successfully.")
