from fastapi import FastAPI, HTTPException, Response, Cookie
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://huzaimafastapi.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks_db = {
    1: {"title": "Finish Database Normalization Assignment", "status": "Done"},
    2: {"title": "Study for COAL Exam", "status": "Procrastinating"},
    3: {"title": "Write deadlock recovery simulation in C", "status": "Pending"}
}

'''huz'''
class taskUpdate(BaseModel):
    status: str

@app.get("/tasks")
def getAllTasks():
    return tasks_db

@app.put("/tasks/{task_id}")
def updateTaskStatus(task_id: int, taskUpdatee: taskUpdate):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    validStatuses = ["Pending", "Done", "Procrastinating"]
    if taskUpdatee.status not in validStatuses:
        raise HTTPException(status_code=400, detail="Invalid Status")
    
    tasks_db[task_id]["status"] = taskUpdatee.status
    return {"message": "Status Updated", "task": tasks_db[task_id]}

class TaskCreate(BaseModel):
    title: str
    completed: bool = False

@app.post("/tasks", status_code=201)
async def create_task(task: TaskCreate):
    await asyncio.sleep(3)
    new_id = max(tasks_db.keys(), default=0) + 1
    tasks_db[new_id] = {"title": task.title, "status": "Pending"}
    
    return {"message": "Task created successfully", "task": tasks_db[new_id]}
class LoginCredentials(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(credentials: LoginCredentials, response: Response):
    if credentials.password != "Huzaima123":
        raise HTTPException(status_code=401, detail="Invalid password!")
    
    response.set_cookie(key="active_user", value=credentials.username, httponly=True)
    return {"message": f"Welcome, {credentials.username}! Cookie dropped."}

@app.get("/whoami")
def check_user(active_user: str | None = Cookie(default=None)):
    if active_user:
        return {"user": active_user} # Return clean data
    return {"user": None}