from typing import Union
from typing import Optional

from pydantic import BaseModel


class CategoryBase(BaseModel):
    id: Optional[int]
    name:str
    
    class Config:
        orm_mode = True
        
class CategoryRequest(CategoryBase):
    ...
    
class CategoryResponse(CategoryBase):
    id: Optional[int]

    class Config:
        orm_mode = True  
