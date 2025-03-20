from fastapi import APIRouter
from app.utils.level_adjustment import adjust_level
from app.utils.story_generator import generate_story, generate_mcqs
from pydantic import BaseModel

router = APIRouter()

class AdjustLevelRequest(BaseModel):
    accuracy: int
    sadness: int
    happiness: int
    engagement: int
    time_spent: int
    current_level: int

class GenerateStoryRequest(BaseModel):
    current_level: int


@router.post("/adjust_level")
async def adjust_level_api(request: AdjustLevelRequest):
    # Adjust level based on the input parameters
    new_level = adjust_level(
        accuracy=request.accuracy,
        sadness=request.sadness,
        happiness=request.happiness,
        engagement=request.engagement,
        time_spent=request.time_spent,
        current_level=request.current_level
    )
    return {"new_level": new_level}


@router.post("/generate_story_and_questions")
async def generate_story_and_questions(request: GenerateStoryRequest):
    # Generate a story and MCQs based on the current level
    story = await generate_story(request.current_level)
    mcqs = await generate_mcqs(story)
    return {
        "story": story,
        "questions": mcqs
    }
