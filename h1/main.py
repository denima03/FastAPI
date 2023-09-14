from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field, HttpUrl
from typing import Annotated
app= FastAPI()
# @app.get('/item/{item_id}')
# async def read_item(item_id):
#     return{"item_id": item_id}

# fake_items_db = [{"item_name": "phone"},{"item_name": "laptop"}]

# @app.get('/items')
# async def read_items(skip: int = 0, limit: int = 3):
#     return fake_items_db[skip: skip + limit]


# multiple parameter
# @app.get ('/users/{user_id/items/{item_id}')
# #async def read_item(item_id: int, desc: str | None = None):\

# async def read_item(user_id: int, item_id: int, desc: str = None, short : bool = False):
#     item = {"item_id": item_id, "owwner_id": user_id}
#     if desc :
#         item.update({"item_id": item_id, "desc": desc})
#     if not short:
#         item.update({"description": "This item whithout short"})
#     return item

#request body

# class Item(BaseModel):
#     name : str
#     description: str = None
#     price : float
#     tax : int = None

# class User(BaseModel):
#     name : str

# @app.post("/items")
# async def create_item(item:Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price * item.tax 
#         item_dict.update({"price_with_tax":price_with_tax})
#     return item_dict

# #String Validasi
# @app.get('/items')
# async def read_items(q: Annotated [str | None, Query(min_length=3,max_length=10)] = None):
#     results = {"items": [{"item_id": "foo"},{"item_id":"bar"}]}
#     if q :
#         results.update({"q":q})
#     return results

# #numeric validation
# @app.get('/items/{item_id}')
# async def read_items(
#     item_id: Annotated[int, Path(title="Id of the item", ge=0, le=10)],
#     q: Annotated[str | None, Query(alias="item-query")]=  None,
#     size: Annotated [float, Query(gt=0, lt=9.5)] = None
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     if size:
#         results.update({"size": size})
#     return results


# mutiple body parameter
# class Item(BaseModel):
#     name : str
#     description: str = None
#     price : float
#     tax : int = None
# class User(BaseModel):
#     uername: str
#     full_name:str = None
# @app.put('/items/{item_id}')
# async def update_item(item_id: int, item: Item, user: User):
#     results ={"item_id": item_id,"item":item,"user": user}
#     return results

# # Body Field
# class User(BaseModel):
#     name: str
#     full_name: str | None = Field(default=None, max_length=10)
#     password: str | None= Field(default= None, min_length=5)

# @app.put("/items/{user_id}")
# async def update_item(user_id:"int", user:"User"):
#     results = {"user_id":user_id, "user": user}
#     return results    

#Nested Model
class Image(BaseModel):
    url: HttpUrl
    name : str



class Item(BaseModel):
    name : str
    description: str = None
    price : float
    tax : int = None
    tags: list[str] = []
    image: list[Image] = None

@app.put('/item/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {"item_id":item_id, "item": item}
    return results

@app.post('/multiple/image')
async def cerate(image:list[Image]):
    return image


