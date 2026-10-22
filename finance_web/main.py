from fastapi import FastAPI
import json
app = FastAPI()

@app.get("/")
def greet_browser():
    return {"message": "hello Welcome to my Finance Tracker"}

@app.get("/about")
def about_fn():
    return {"message": "This is my Finance Tracker"}

@app.get("/expenses/{serial_no}")
def get_value(serial_no : int ,q:str | None= None):
    with open("data.json", "r") as file:
            loaded_dict = json.load(file)
            return loaded_dict[serial_no]