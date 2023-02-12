# Importa a classe FastAPI da biblioteca fastapi
from fastapi import FastAPI

# Importa as rotas
from routes import Category_router
from routes import Product_router

from automat_db.create_tables import *
from automat_db.create_db import *

create_db() # verifica se o banco de dados ja está criado caso contrário cria
create_tables() # verofoca se as tabelas já foram criadas

# Cria uma instância da classe FastAPI
app = FastAPI()

# Inclui a rota da categoria na aplicação
app.include_router(Category_router.router, tags=['categories'])

# Inclui a rota do produto na aplicação
app.include_router(Product_router.router, tags=['products'])