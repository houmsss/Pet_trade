from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import datetime


class GoodsAdd(BaseModel):
    name: str
    description: Optional[str] = None
    price: str


class Goods(GoodsAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class GoodsID(BaseModel):
    ok: bool = True
    good_id: int


class BuyerADD(BaseModel):
    first_name: str = Field()
    last_name: str = Field()
    birthdate: datetime = Field()


class Buyer(BuyerADD):
    id: int
    model_config = ConfigDict(from_attributes=True)


class BuyerID(BaseModel):
    ok: bool = True
    buyer_id: int
