from typing import Optional

from fastapi import Fastapi
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
		name:str
		description:Optional[str] = None
		price:float
		tax:Optional[float]=None
		tags:list=[]


@app.put("/items/{item_id}")
async def update_item(item_id:int,item:Item):
		results = {"item_id":item_id,"item":item}
		return results