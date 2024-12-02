from fastapi import APIRouter, HTTPException
from app.models import ChildProgress
from app.database import save_progress, get_progress

router = APIRouter()

@router.post("/save_progress/")
async def save_child_progress(progress: ChildProgress):
    try:
        save_progress(progress)
        return {"message": "Child progress saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving progress: {str(e)}")

@router.get("/get_progress/{child_id}")
async def retrieve_child_progress(child_id: str):
    progress = get_progress(child_id)
    if not progress:
        raise HTTPException(status_code=404, detail="Child progress not found")
    return progress
