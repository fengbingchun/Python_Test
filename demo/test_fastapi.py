from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

# Blog: https://blog.csdn.net/fengbingchun/article/details/148201339

app = FastAPI()

class Item(BaseModel):
	name: str
	price: float
	is_offer: Union[bool, None] = None

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/")
def read_root():
	return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None): # q is a query parameter, q is optional, its length doesn't exceed 50 characters
	return {"item_id": item_id, "q": q}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items2/")
async def read_item2(skip: int = 0, limit: int = 10): # Query Parameters
    return fake_items_db[skip : skip + limit]