# import sqlite3

# # Connect to database (creates file if not exists)
# conn = sqlite3.connect("expenses.db")

# cursor = conn.cursor()

# # Create table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS expenses (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     category TEXT,
#     amount REAL
# )
# """)

# conn.commit()

# print("Database and table created successfully!")

# conn.close()

# import sqlite3

# conn = sqlite3.connect("expenses.db")
# cursor = conn.cursor()

# # Insert expense
# cursor.execute("INSERT INTO expenses (category, amount) VALUES (?, ?)", ("food", 500))
# cursor.execute("INSERT INTO expenses (category, amount) VALUES (?, ?)", ("movie", 1000))

# conn.commit()

# print("Data inserted successfully!")

# conn.close()

import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()

for row in rows:
    print(row)
# cursor.execute("UPDATE expenses SET amount = ? WHERE category = ?", (600, "food"))
# conn.commit()
# cursor.execute("DELETE FROM expenses WHERE category = ?", ("movie",))
conn.commit()
conn.close()