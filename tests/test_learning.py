from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch, AsyncMock

client = TestClient(app)


@patch.dict('os.environ', {'OPENAI_API_KEY': 'fake-api-key'})
@patch('app.utils.story_generator.generate_story')
@patch('app.utils.story_generator.generate_mcqs')
async def test_submit_feedback(mock_generate_mcqs, mock_generate_story):
    # Setup async mocks
    mock_generate_story.return_value = "Test story"
    mock_generate_mcqs.return_value = "Test questions"
    mock_generate_story.side_effect = AsyncMock(return_value="Test story")
    mock_generate_mcqs.side_effect = AsyncMock(return_value="Test questions")

    response = client.post(
        "/api/submit_feedback/",
        json={
            "child_id": "123",
            "question_accuracy": 85,
            "question_time": 25,
            "emotional_feedback": {
                "sadness": 10,
                "happiness": 90,
                "engagement": 75
            },
            "current_level": 1
        }
    )
    assert response.status_code == 200
    assert "new_level" in response.json()