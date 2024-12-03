import pytest
from unittest.mock import patch
from app.utils.story_generator import generate_story, generate_mcqs


@pytest.mark.asyncio
@patch.dict('os.environ', {'OPENAI_API_KEY': 'fake-api-key'})
@patch("openai.chat.completions.acreate")
async def test_generate_story(mock_openai):
    mock_openai.return_value = {
        "choices": [{"message": {"content": "Once upon a time..."}}]
    }
    story = await generate_story(1)
    assert "Once upon a time" in story


@pytest.mark.asyncio
@patch.dict('os.environ', {'OPENAI_API_KEY': 'fake-api-key'})
@patch("openai.chat.completions.acreate")
async def test_generate_mcqs(mock_openai):
    mock_openai.return_value = {
        "choices": [{"message": {"content": "1. What is the story about? (a) A cat..."}}]
    }
    story = "This is a test story."
    mcqs = await generate_mcqs(story)
    assert "What is" in mcqs
