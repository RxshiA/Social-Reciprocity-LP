from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_submit_feedback():
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
    assert isinstance(data["questions"], str)  # Verify questions are generated as a string
