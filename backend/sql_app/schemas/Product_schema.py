from typing import Union
from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    id: Optional[int]
    name:str
    category: int
    price: float
    serie: int
    
    class Config:
        orm_mode = True
        
class ProductRequest(ProductBase):
    ...
    
class ProductResponse(ProductBase):
    id: Optional[int]
    name:str
    category: int
    price: float
    serie: int

    class Config:
        orm_mode = True  
