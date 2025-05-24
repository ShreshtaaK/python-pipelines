import sqlite3
import json
import os
import sys
import subprocess

conn = sqlite3.connect('mydb.sqlite')
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM Customer")
customer_count = cursor.fetchone()[0]
print(f"Customer count: {customer_count}")

if customer_count > 500:
    cursor.execute("SELECT * FROM Customer")
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    data = [dict(zip(columns, row)) for row in rows]

    with open("customer_data.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print("Customer data exported to customer_data.json")

    if customer_count > 600:
        print("Triggering child pipeline (product export)...")
        child_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "child_pipeline.py")
        print(f"Child pipeline path: {child_script_path}")
        print(f"Exists? {os.path.isfile(child_script_path)}")

        result = subprocess.run([sys.executable, child_script_path], capture_output=True, text=True)

        print("Child pipeline output:")
        print(result.stdout)
        if result.stderr:
            print("Child pipeline errors:")
            print(result.stderr)

else:
    print("Customer count is less than 500. No action taken.")

conn.close()
