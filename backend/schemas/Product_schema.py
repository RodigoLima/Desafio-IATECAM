from typing import Optional

from pydantic import BaseModel as SCBaseMode

class CategorySchema(SCBaseMode):
    id: Optional[int]
    name:str
    category: int
    price: float
    serie: int
    
    class config:
        orm_mode = True