from typing import Union
from typing import Optional

from pydantic import BaseModel

class CategoryBase(BaseModel):
    id: Optional[int]
    name: str
    
class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: Optional[int]
    name:str
    
    class Config:
        orm_mode = True
        
class ProductBase(BaseModel):
    id: Optional[int]
    name:str
    category: int
    price: float
    serie: int
    
class ProductCreate(CategoryBase):
    pass

class Product(ProductBase):
    id: Optional[int]
    name:str
    category: int
    price: float
    serie: int
    
    class Config:
        orm_mode = True