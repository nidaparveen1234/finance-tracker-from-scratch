from fastapi import FastAPI
import json
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def greet_browser():
    return {"message": "hello Welcome to my Finance Tracker"}

@app.get("/about")
def about_fn():
    return {"message": "This is my Finance Tracker"}

@app.get("/expenses/{serial_no}")
def get_value(serial_no: str):
    with open("../finance/data.json", "r") as file:
            loaded_dict = json.load(file)
            return loaded_dict[serial_no]

@app.get("/expenses")
def get_all():
     with open("../finance/data.json", "r") as file:
          loaded_dict = json.load(file)
          return loaded_dict
     
class Expenses(BaseModel):
     Expense : int
     Category: str
     Date: str

@app.post("/expenses")
def add_expense(expense: Expenses):
     with open("../finance/data.json", "r") as file:
        loaded_dict = json.load(file)
        serial = len(loaded_dict) + 1
        loaded_dict[serial] = {
             "Expense": expense.Expense,
             "Category": expense.Category,
             "Date": expense.Date
             }
     with open("../finance/data.json", "w") as file:
          json.dump()