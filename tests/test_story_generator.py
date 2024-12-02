from unittest.mock import patch
from app.utils.story_generator import generate_story, generate_mcqs

@patch("openai.ChatCompletion.create")
def test_generate_story(mock_openai):
    mock_openai.return_value = {
        "choices": [{"message": {"content": "Once upon a time..."}}]
    }
    story = generate_story(1)
    assert isinstance(story, str)
    assert "Once upon a time" in story

@patch("openai.ChatCompletion.create")
def test_generate_mcqs(mock_openai):
    mock_openai.return_value = {
        "choices": [{"message": {"content": "1. What is the story about? (a) A cat..."}}]
    }
    story = "This is a test story."
    mcqs = generate_mcqs(story)
    assert isinstance(mcqs, str)
    assert "What is the story about" in mcqs
