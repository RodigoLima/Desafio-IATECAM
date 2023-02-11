from core.configs import settings

from sqlalchemy import Column, Integer, String,ForeignKey,Float

class ProductModel(settings.DBBaseModel):
    __tablename = "Product"
    
    id: int = Column(Integer, primary_key=True,autoincrement=True)  
    name: str = Column(String(60),nullable=False)  
    category: int =  Column(Integer, ForeignKey('Category.id'),nullable=False)
    price: float = Column(Float,nullable=False)
    serie: int - Column(Integer,nullable=False)