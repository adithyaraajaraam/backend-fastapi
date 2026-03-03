from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

expenses = []

class Expense(BaseModel):
    category: str
    amount: float

@app.get("/")
def home():
    return {"message": "Expense Tracker API Running"}

@app.post("/expense")
def add_expense(expense: Expense):
    expenses.append(expense)
    return {"message": "Expense added successfully"}

@app.get("/expenses")
def get_expenses():
    return expenses

@app.get("/total")
def total_spent():
    total = sum(exp.amount for exp in expenses)
    return {"total_spent": total}

@app.get("/highest")
def highest_expense():
    if not expenses:
        return {"message": "No expenses available"}

    highest = max(expenses, key=lambda x: x.amount)
    return {
        "category": highest.category,
        "amount": highest.amount
    }

@app.get("/category/{name}")
def get_by_category(name: str):
    filtered = [exp for exp in expenses if exp.category.lower() == name.lower()]

    if not filtered:
        return {"message": "No expenses found for this category"}

    return filtered