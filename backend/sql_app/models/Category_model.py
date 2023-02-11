
from core.database import Base
from sqlalchemy import Column, Integer, String,ForeignKey,Float

class Category(Base):
    __tablename__ = "category"
    
    id: int = Column(Integer, primary_key=True,autoincrement=True)  
    name: str = Column(String(128),nullable=False)  
    

