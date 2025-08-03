# POST Data: Receiving JSON in the Request Body
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name : str = Field(..., min_length=3, description="The name of the item")
    description : Optional[str] = None
    price: float = Field(...,gt=0, description='The price must be greater than zero')
    tax: Optional[float] = Field(None, gt=0)

@app.post("/items/create")
async def create_item(item: Item):
    # In a real application, you would save the item to a database here.
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict