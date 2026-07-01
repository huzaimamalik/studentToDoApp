from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

def test_get_all_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert "2" in response.json()

def test_update_task():
    response = client.put("/tasks/3", json={"status": "Done"})
    assert response.status_code == 200
    assert response.json()["task"]["status"] == "Done"