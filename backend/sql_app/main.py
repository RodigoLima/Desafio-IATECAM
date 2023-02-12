# Importa a classe FastAPI da biblioteca fastapi
from fastapi import FastAPI
import uvicorn
# Importa as rotas
from routes import Category_router
from routes import Product_router

from fastapi.middleware.cors import CORSMiddleware

from automat_db.create_tables import *
from automat_db.create_db import *

create_db() # verifica se o banco de dados ja está criado caso contrário cria
create_tables() # verofoca se as tabelas já foram criadas

# Cria uma instância da classe FastAPI
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Inclui a rota da categoria na aplicação
app.include_router(Category_router.router, tags=['categories'])

# Inclui a rota do produto na aplicação
app.include_router(Product_router.router, tags=['products'])

