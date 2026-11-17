from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Minha primeira pipeline CI/CD!"}

@app.get("/health")
def health():
    return {"status": "ok"}
