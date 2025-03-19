from fastapi import FastAPI
from app.routes import learning
from app.routes import progress

app = FastAPI()

# Include routes
app.include_router(learning.router, prefix="/api", tags=["Learning"])
app.include_router(progress.router, prefix="/api", tags=["Progress"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Adaptive Learning API"}
 