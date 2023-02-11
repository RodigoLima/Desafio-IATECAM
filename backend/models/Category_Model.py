from core.configs import settings

from sqlalchemy import Column, Integer, String

class CategoryModel(settings.DBBaseModel):
    __tablename = "Category"
    
    id: int = Column(Integer, primary_key=True,autoincrement=True)  
    name: str = Column(String(128),nullable=False)  