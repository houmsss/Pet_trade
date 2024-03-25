from sqlalchemy import select

from models import GoodsAdd, Goods, BuyerADD, Buyer
from database import new_session, GoodsOrm, BuyerOrm


class GoodsRepository:
    @classmethod
    async def add_one(cls, data: GoodsAdd) -> int:
        async with new_session() as session:
            goods_dict = data.model_dump()

            good = GoodsOrm(**goods_dict)
            session.add(good)
            await session.flush()
            await session.commit()
            return good.id

    @classmethod
    async def get_all(cls) -> list[Goods]:
        async with new_session() as session:
            query = select(GoodsOrm)
            result = await session.execute(query)
            goods_models = result.scalars().all()
            goods_shemas = [Goods.validate(good_model) for good_model in goods_models]
            return goods_shemas
