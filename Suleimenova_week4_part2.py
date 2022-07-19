from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to my page!"

@app.get("/home")
def read_home():
    return "I'll try to make site about cats"

# @app.get("/info")

# @app.get("/facts")