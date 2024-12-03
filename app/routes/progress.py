from fastapi import APIRouter, HTTPException
from app.models import ChildProgress
from app.database import save_progress, get_progress
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

router = APIRouter()


def custom_jsonable_encoder(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, dict):
        return {k: custom_jsonable_encoder(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [custom_jsonable_encoder(i) for i in obj]
    return jsonable_encoder(obj)


@router.post("/save_progress/")
async def save_child_progress(progress: ChildProgress):
    try:
        save_progress(progress)
        return {"message": "Child progress saved successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error saving progress: {str(e)}")


@router.get("/get_progress/{child_id}")
async def retrieve_child_progress(child_id: str):
    progress = get_progress(child_id)
    if not progress:
        raise HTTPException(status_code=404, detail="Child progress not found")
    return custom_jsonable_encoder(dict(progress))
