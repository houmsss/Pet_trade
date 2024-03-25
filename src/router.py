from typing import Annotated
from fastapi import APIRouter, Depends

from models import GoodsAdd, GoodsID, Goods
from repository import GoodsRepository

goods_router = APIRouter(
    prefix="/goods",
    tags=["Товары"]
)

buyers_router = APIRouter(
    prefix="/buyer",
    tags=["Покупатели"]
)


@goods_router.post("")
async def add_good(good: Annotated[GoodsAdd, Depends()]) -> GoodsID:
    good_id = await GoodsRepository.add_one(good)
    return {"ok": True, "good_id": good_id}


@goods_router.get("")
async def get_goods() -> list[Goods]:
    goods = await GoodsRepository.get_all()
    return goods


@buyers_router.get("")
async def get_buyers() -> list:
    return ['buy1', 'buy2', 'buy3']
