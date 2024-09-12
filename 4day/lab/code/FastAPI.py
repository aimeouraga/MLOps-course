
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Create a FastAPI instance
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return "Hello world"

# Health endpoint
@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "up and running"})
