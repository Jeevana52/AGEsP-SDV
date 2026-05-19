from fastapi import FastAPI

app = FastAPI(title="diagnostics reporting-service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/faults")
def faults():
    return {"faults": []}
