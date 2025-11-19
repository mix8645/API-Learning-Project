from typing import Union
from fastapi import FastAPI, Request
from model.schemas import Item

app = FastAPI()

@app.get("/hello")
def hello_word():
    return {
        "message": "Hello Word!!"
    }
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {
        "item_id": item_id,
        "q": q
    }
    
@app.post("/items")
def create_item(item: Item):
    return { 
            "requst_body": item
        }

@app.put("/items/{item_id}")
def edit_item(item_id: int, item: Item):
    return { 
            "id": item_id, 
            "request_body": item
        }