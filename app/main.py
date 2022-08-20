"""My Module"""

from typing import Union
from bson import Decimal128
from fastapi import FastAPI
from app.db import client


app = FastAPI()


@app.get("/")
async def read_root():
    """read_root"""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, query: Union[str, None] = None):
    """read_item"""
    return {"item_id": item_id, "q": query}


@app.get("/zee")
async def read_zee():
    """read_zee"""
    return {"What": "Up"}


@app.get("/airbnb")
async def read_airbnb():
    """get top 10 reviews for the airbnb collection"""
    col = client()["sample_airbnb"]["listingsAndReviews"]
    lst = []
    for doc in col.find({}, {"_id": False}).limit(10):
        encoded = {k: v.to_decimal() if isinstance(v, Decimal128) else v for k, v in doc.items()}
        lst.append(encoded)
    return lst
