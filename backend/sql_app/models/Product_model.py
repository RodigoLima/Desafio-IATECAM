# Importa a classe Base da biblioteca 'database'
from core.database import Base

# Importa as classes necessárias para definir colunas em uma tabela de banco de dados
from sqlalchemy import Column, Integer, String,ForeignKey,Float

class Product(Base):
    """
    Classe que representa a tabela 'product' no banco de dados. Cada instância dessa classe 
    representa uma linha na tabela que armazena informações sobre os produtos no sistema.
    """
    # Nome da tabela no banco de dados
    __tablename__ = "product"
    
    # Coluna 'id' da tabela
    id: int = Column(Integer, primary_key=True,autoincrement=True,doc="Id do Produto")  
    
    # Coluna 'name' da tabela
    name: str = Column(String(60),nullable=False,doc="Nome do Produto")  
    
    # Coluna 'category' da tabela
    category: int =  Column(Integer, ForeignKey('category.id'),nullable=False,doc="Id da Categoria")
    
    #Coluna 'price' da tabela
    price: float = Column(Float,nullable=False,doc="Preço do Produto")
    
    #Coluna 'serie' da tabela
    serie: int = Column(Integer,nullable=False,doc="Serie do Produto")