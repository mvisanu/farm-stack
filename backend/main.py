from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo

app = FastAPI()

from database import (
  fetch_one_todo,
  fetch_all_todos,
  create_todo,
  update_todo,
  remove_todo,
)

origins = ['http://localhost:3000']

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials = True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def read_root():
  return {"Server": "Started"}

@app.get("/api/todo")
async def get_todo():
  response = await fetch_all_todos()
  return response

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title):
  response = await fetch_one_todo(title)
  if response:
    return response
  raise HTTPException(404, f"there is no TODO item with this {title}")
 

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
  record = {"title": todo.title, "description": todo.description}  
  response = await create_todo(record)
  if response:
    return "Todo created successfully"
  raise HTTPException(400, "Something went wrong or bad request")

@app.put("/api/todo/{title}", response_model=Todo)
async def put_todo(title:str, desc:str):
  response = await update_todo(title, desc)
  if response:
    return response
  raise HTTPException(404, f"there is no TODO item with this {title}")

@app.delete("/api/todo/{title}")
async def delete_todo(title):
  response = await remove_todo(title)
  if response:
    return "Successfully deleted todo item !"
  raise HTTPException(404, f"there is no TODO item with this {title}")
  
  return True