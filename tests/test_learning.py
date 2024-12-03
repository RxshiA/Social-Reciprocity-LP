from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch, AsyncMock

client = TestClient(app)


@patch.dict('os.environ', {'OPENAI_API_KEY': 'fake-api-key'})
@patch('app.utils.story_generator.generate_story')
@patch('app.utils.story_generator.generate_mcqs')
def test_submit_feedback(mock_generate_mcqs, mock_generate_story):
    # Setup mocks
    mock_generate_story.return_value = "Test story"
    mock_generate_mcqs.return_value = "Test questions"

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
    data = response.json()
    assert "new_level" in data
    assert "story" in data
    assert "questions" in data
    assert isinstance(data["questions"], str)
