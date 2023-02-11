from typing import Optional

from pydantic import BaseModel as SCBaseMode

class CategorySchema(SCBaseMode):
    id: Optional[int]
    name:str
    
    
    class config:
        orm_mode = True