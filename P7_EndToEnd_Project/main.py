from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

DATABASE = "expenses.db"

# ----------------------------
# Database Initialization
# ----------------------------
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        amount REAL
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ----------------------------
# Pydantic Model
# ----------------------------
class Expense(BaseModel):
    category: str
    amount: float

# ----------------------------
# Routes
# ----------------------------

@app.get("/")
def home():
    return {"message": "Expense Tracker API with Database"}

@app.post("/expense")
def add_expense(expense: Expense):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (category, amount) VALUES (?, ?)",
        (expense.category, expense.amount)
    )

    conn.commit()
    conn.close()

    return {"message": "Expense added successfully"}

@app.get("/expenses")
def get_expenses():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "category": row[1],
            "amount": row[2]
        })

    return result

@app.get("/total")
def total_spent():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    conn.close()

    return {"total_spent": total if total else 0}

@app.delete("/expense/{expense_id}")
def delete_expense(expense_id: int):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return {"message": "Expense not found"}

    conn.close()
    return {"message": "Expense deleted successfully"}