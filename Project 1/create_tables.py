import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('mydb.sqlite')
cursor = conn.cursor()

# Create Customer table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        country TEXT NOT NULL
    )
''')

# Create Product table (optional for later steps)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        price REAL NOT NULL
    )
''')

# Optional: Insert sample data into Customer
customers = [
    ('John Doe', 'john@example.com', 'India'),
    ('Jane Smith', 'jane@example.com', 'US'),
    ('Alice Johnson', 'alice@example.com', 'UK')
]

cursor.executemany('INSERT INTO Customer (name, email, country) VALUES (?, ?, ?)', customers)

# Commit changes and close connection
conn.commit()
conn.close()

print("Tables created and sample data inserted successfully.")
