from fastapi import FastAPI

app = FastAPI(title="ecu failure detection-service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/faults")
def faults():
    return {"faults": []}
