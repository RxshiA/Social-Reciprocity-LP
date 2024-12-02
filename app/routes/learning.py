from fastapi import APIRouter
from app.utils.level_adjustment import adjust_level
from app.utils.story_generator import generate_story, generate_mcqs
from app.models import ChildProgress

router = APIRouter()

@router.post("/submit_feedback/")
async def submit_feedback(progress: ChildProgress):
    # Adjust level based on progress
    new_level = adjust_level(
        accuracy=progress.question_accuracy,
        sadness=progress.emotional_feedback.sadness,
        happiness=progress.emotional_feedback.happiness,
        current_level=progress.current_level
    )
    
    # Generate a new story and MCQs for the child
    story = await generate_story(new_level)
    mcqs = await generate_mcqs(story)
    
    return {
        "new_level": new_level,
        "story": story,
        "questions": mcqs
    }
