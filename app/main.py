"""My Module"""

from typing import Union

from fastapi import FastAPI

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
    