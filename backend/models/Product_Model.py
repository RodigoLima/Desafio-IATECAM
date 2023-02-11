from core.configs import settings

from sqlalchemy import Column, Integer, String,ForeignKey

class ProductModel(settings.DBBaseModel):
    __tablename = "Product"
    
    id: int = Column(Integer, primary_key=True,autoincrement=True)  
    name: str = Column(String(60))  
    category: int =  Column(Integer, ForeignKey('Category.id'))