from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def ping():
    return {"status": "ok"}
