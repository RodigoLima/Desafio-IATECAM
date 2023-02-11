from fastapi import FastAPI

from routes import Category_router
from routes import Product_router

from core.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(Category_router.router, tags=['categories'])
app.include_router(Product_router.router, tags=['products'])