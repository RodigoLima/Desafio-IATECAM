# Importação dos tipos Optional do módulo typing
from typing import Optional

# Importação da classe BaseModel do módulo pydantic
from pydantic import BaseModel

# Classe base de produto que define os atributos básicos de um produto
class ProductBase(BaseModel):
    # ID do produto (opcional)
    id: Optional[int]
    # Nome do produto
    name:str
    # Categoria do produto
    category: int
    # Preço do produto
    price: float
    # Série do produto
    serie: int

    class Config:
        orm_mode = True

# Classe que representa a requisição de um produto
class ProductRequest(ProductBase):
    # Herdando todos os atributos da classe ProductBase
    ...

# Classe que representa a resposta de uma requisição de produto
class ProductResponse(ProductBase):
    # ID do produto (opcional)
    id: Optional[int]
    # Nome do produto
    name:str
    # Categoria do produto
    category: int
    # Preço do produto
    price: float
    # Série do produto
    serie: int

    class Config:
        orm_mode = True
