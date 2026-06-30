from fastapi.testclient import testClient
from main import app
client = testClient(app)

def testGetAllTasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert data["2"]["title"] == "Study For COAL Exam"

def taskUpdateTaskStatusSuccess():
    response=client.put("/tasks/3", json={"status": "Done"})
    assert response.status_code==200
    assert response.json()["task"]["status"]=="Done"

def testUpdateTaskInvalidStatus():
    response = client.put("/tasks/1", json={"status": "Huzaima"})
    assert response.status_code == 400
    
