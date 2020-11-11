# -*- coding: utf-8 -*-
import uvicorn
from fastapi import BackgroundTasks, Depends, FastAPI
import time
import traceback

from alchemydb import Session, engine
from models import Tasks
from pydantic import BaseModel

from sqlutils import alchemytojson, alchemytodict
from todo import add_todo
from todo import delete_todo
from todo import update_todo
from todo import get_todo
from todo import get_todo_list

class AddTodo(BaseModel):
    name: str
    text: str

api = FastAPI(
   cors=True,
   allowed_hosts=["*"],
)

@api.get("/")
def index():
    item = {
        "message": "Hello World"
    }
    return item

@api.get("/api/todo/{id}")
def on_get(id: int):
    todo = get_todo(id)
    item = {
        "status": True,
        "todo": todo
    }
    return item

@api.get("/api/todo")
def on_get():
    todos = get_todo_list()
    item = { 
        "status": True, 
        "todos": todos 
    }
    return item

@api.post("/api/todo")
async def on_post(addtodo: AddTodo):
    def process_add_todo(name, text):
        time.sleep(3)
        add_todo(name, text)
    process_add_todo(addtodo.name, addtodo.text)
    item = {
        'status': True
    }
    return item

@api.put("/api/todo/{id}")
async def on_put(self, req, resp, *, id):
    def process_update_todo(name, text):
        time.sleep(3)
        update_todo(id, name, text)
    data = await req.media()
    name = data['name']
    text = data['text']
    process_update_todo(name, text)
    resp.media = {
        'status': True
    }
    
@api.delete("/api/todo/{id}")
async def on_delete(self, req, resp, *, id):
    def process_delete_todo():
        time.sleep(3)
        delete_todo(id)
    process_delete_todo()
    resp.media = {
        'status': True
    }


if __name__ == "__main__":
   uvicorn.run(api,host="0.0.0.0", port=8000)