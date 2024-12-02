from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.db.save_progress")
def test_save_progress(mock_save_progress):
    mock_save_progress.return_value = None
    response = client.post(
        "/api/save_progress/",
        json={
            "child_id": "123",
            "question_accuracy": 85,
            "question_time": 20,
            "emotional_feedback": {
                "sadness": 20,
                "happiness": 80,
                "engagement": 70
            },
            "current_level": 2
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Child progress saved successfully"}

@patch("app.db.get_progress")
def test_get_progress(mock_get_progress):
    mock_get_progress.return_value = {
        "child_id": "123",
        "question_accuracy": 85,
        "emotional_feedback": {
            "sadness": 20,
            "happiness": 80,
            "engagement": 70
        },
        "current_level": 2
    }
    response = client.get("/api/get_progress/123")
    assert response.status_code == 200
    data = response.json()
    assert data["child_id"] == "123"
    assert data["current_level"] == 2
