from pydantic import BaseModel

class Todo(BaseModel):
  title: str = None
  description: str = None
  

 