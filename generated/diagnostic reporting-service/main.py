from fastapi import FastAPI

app = FastAPI(title="diagnostic reporting-service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/faults")
def faults():
    return {"faults": []}
