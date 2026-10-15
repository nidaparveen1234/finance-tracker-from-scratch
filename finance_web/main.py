from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet_browser():
    return {"message": "hello"}