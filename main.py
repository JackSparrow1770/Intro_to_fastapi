from enum import Enum
from fastapi import FastAPI, Query
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/{item_id}")
async def reading(item_id : int):
    return {"item_id": item_id, "type": type(item_id).__name__}


# use of enum class
class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnetb4u"
    lenet = "lenet4500"

@app.get("/models/{model_name}")
async def get_model(model_name : ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message":"this is DL model"}
    if model_name.value == "lenet4500":
        return {"model_name": model_name, "message":"Lenet400 it is"}
    return {"model_name": model_name, "message": "Have some residuals"}

## filtering and Pagination
# Default values
fake_items_db =[]    #in memory data

@app.get("/items/")
async def reading_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip+limit]

# note : A request to /items/ is equivalent to /items/?skip=0&limit=10.

# Truely optional parameters
@app.get("/items/{item_id}")
async def read_item(item_id: str, q : Optional[str] = None):
    if q:
        return {"item_id": item_id, "q":q}
    return {"item_id": item_id}

#Required parameters : simply declare it with default value
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# list parameters : to accept multiple values for a single query parameter
@app.get("/items/")
async def read_items(tags: Optional[List[str]] = Query(None) ):
    query_items = {"tags": tags}
    return query_items

#Request Body : complex Data Structures
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


