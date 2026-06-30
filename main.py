from fastapi import FastAPI, HTTPException
from pydantic import baseModel
app = FastAPI()
tasks_db = {
    1: {"title": "Finish Database Normalization Assignment", "status": "Done"},
    2: {"title": "Study for COAL Exam", "status": "Procrastinating"},
    3: {"title": "Write deadlock recovery simulation in C", "status": "Pending"}
}

class taskUpdate(baseModel)
    status: str
@app.get("/tasks")
def getAllTasks():
    return tasks_db

@app.put("/tasks/{task_id}")
def updateTaskStatus(task_id: int, taskUpdatee: taskUpdate)
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    validStatuses = ["Pending", "Done", "Procrastinating"]
    if taskUpdatee.status not in validStatuses:
        raise HTTPException(status_code=400, detail="Invalid Status")
    tasks_db[task_id]["status"]=taskUpdatee.status
    return{"message": "Status Updated", "task": tasks_db[task_id]}