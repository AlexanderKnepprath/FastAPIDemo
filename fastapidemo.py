from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# create application
app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []

# default route
@app.get("/")
def root():
    return {"Hello": "World"}

# add items to list (via ''' curl.exe -X POST -H "Content-Type: application/json" -d "{"text":"{task}"}" 'http://127.0.0.1:8000/items' ''')
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

# get first 'x' items in list (via ''' curl.exe -X GET 'http://127.0.0.1:8000/items?limit={limit}' ''')
@app.get("/items")
def list_items(limit: int = 10):
    return items[0:limit]

# get a particular item from list (via ''' curl.exe -X GET 'http://127.0.0.1:8000/items/{item_id}' ''')
@app.get('/items/{item_id}')
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        # error response handling
        raise HTTPException(status_code=404, detail="Error 404: Item not found in list.")