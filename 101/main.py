from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def root():
    return { "message": "Hello World"}


@app.get("/ashish")
def ashish():
    return { "message": "Ashish Welcome to New World"}

