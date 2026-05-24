from fastapi import FastAPI

app = FastAPI()

VERSION = "1.0.0"

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "Hello from DevOps project"}

@app.get("/version")
def version():
    return {"version": VERSION}
