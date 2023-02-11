
from core.database import Base
from sqlalchemy import Column, Integer, String,ForeignKey,Float

class Product(Base):
    __tablename__ = "product"
    
    id: int = Column(Integer, primary_key=True,autoincrement=True)  
    name: str = Column(String(60),nullable=False)  
    category: int =  Column(Integer, ForeignKey('category.id'),nullable=False)
    price: float = Column(Float,nullable=False)
    serie: int = Column(Integer,nullable=False)  
    

