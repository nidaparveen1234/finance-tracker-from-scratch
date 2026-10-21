from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet_browser():
    return {"message": "hello Welcome to my Finance Tracker"}

@app.get("/about")
def about_fn():
    return {"message": "This is my Finance Tracker"}