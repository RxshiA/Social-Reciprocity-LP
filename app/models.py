from pydantic import BaseModel
from typing import Optional

class EmotionalFeedback(BaseModel):
    sadness: float  # 0-100
    happiness: float  # 0-100
    engagement: float  # 0-100

class ChildProgress(BaseModel):
    child_id: str
    question_accuracy: float  # Percentage of correct answers
    question_time: Optional[float]  # Time spent per question
    emotional_feedback: EmotionalFeedback
    current_level: int
