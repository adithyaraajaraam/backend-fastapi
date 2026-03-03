from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

expenses = []

class Expense(BaseModel):
    category: str
    amount: float

@app.get("/")
def home():
    return {"message": "FastAPI is working!"}

@app.post("/expense")
def add_expense(expense: Expense):
    expenses.append(expense)
    return {"message": "Expense added successfully"}

@app.get("/expenses")
def get_expenses():
    return expenses