from fastapi import FastAPI
from pydantic import BaseModel

from utils import load_expenses, update_expenses

app = FastAPI()

class Expense(BaseModel):
    amount : int
    category : str
    user : str

# can add filepath into env variables
expenses = load_expenses("./expenses.json")

@app.get("/")
def root():
    return "Welcome to Expenses Analytics Demo !"

@app.get("/expenses")
def get_expenses():
    return expenses

@app.get("/total")
def total():
    return {"total" : sum(t["amount"] for t in expenses)}

@app.post("/expenses")
def add_expense(expense : Expense):
    expenses.append(expense.model_dump())
    update_expenses("./expenses.json", expenses)
    
    return {
        "status" : "added",
        "expense" : expense
    }
    
@app.get("/total/category/{category}")
def total_category(category : str):
    return {
        f"total {category}" : sum(t["amount"] for t in expenses if t["category"] == category)
    }

@app.get("/total/user/{user}")
def total_user(user : str):
    return {
        f"total {user}" : sum(t["amount"] for t in expenses if t["user"] == user)
    }
    
@app.delete("/expenses/{index}")
def delete_expense(index: int):

    deleted = expenses.pop(index)

    update_expenses("./expenses.json", expenses)

    return {
        "status": "deleted",
        "expense": deleted
    }