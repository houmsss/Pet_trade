from fastapi import FastAPI
from database import create_tables, drop_tables
from contextlib import asynccontextmanager

from router import goods_router, buyers_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print('База очищена')
    await create_tables()
    print('Таблицы созданы')
    yield
    print('Приложение остановлено')


app = FastAPI(lifespan=lifespan)
app.include_router(goods_router)
app.include_router(buyers_router)
