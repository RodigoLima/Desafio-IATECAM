from typing import Union
from typing import Optional

from pydantic import BaseModel


class Category(BaseModel):
    id: Optional[int]
    name:str
    
    class Config:
        orm_mode = True
        
class Product(BaseModel):
    id: Optional[int]
    name:str
    category: int
    price: float
    serie: int
    
    class Config:
        orm_mode = True