from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch, MagicMock
from bson import ObjectId
import pytest
import os

client = TestClient(app)


@pytest.fixture(autouse=True)
def mock_environment():
    with patch.dict(os.environ, {"TESTING": "true"}):
        yield


@pytest.fixture(autouse=True)
def mock_db():
    with patch("app.database.db") as mock_db:
        mock_db.child_progress = MagicMock()
        yield mock_db


@patch("app.database.save_progress")
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


# @patch("app.database.get_progress")
# def test_get_progress(mock_get_progress):
#     test_id = ObjectId()
#     mock_data = {
#         "_id": test_id,
#         "child_id": "123",
#         "question_accuracy": 85,
#         "emotional_feedback": {
#             "sadness": 20,
#             "happiness": 80,
#             "engagement": 70
#         },
#         "current_level": 2
#     }
#     mock_get_progress.return_value = mock_data

#     response = client.get("/api/get_progress/123")
#     assert response.status_code == 200

#     data = response.json()
#     print("Response data:", data)  # Debug print

#     assert "_id" in data
#     assert data["_id"] == str(test_id)
#     assert data["child_id"] == "123"
#     assert data["question_accuracy"] == 85
#     assert data["current_level"] == 2
#     assert "emotional_feedback" in data
