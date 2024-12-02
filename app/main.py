from fastapi import FastAPI
from app.routes import learning

app = FastAPI()

# Include routes
app.include_router(learning.router, prefix="/api", tags=["Learning"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Adaptive Learning API"}
