# Importa as classes necessárias para definir colunas em uma tabela de banco de dados
from sqlalchemy import Column, Integer, String

# Importa a classe Base da biblioteca 'database'
from core.database import Base

class Category(Base):
    """
    Classe que representa a tabela 'category' no banco de dados. Cada instância dessa classe 
    representa uma linha na tabela que armazena as informações sobre uma categoria dos produtos no sistema.
    """
    
    # Nome da tabela no banco de dados
    __tablename__ = "category"
    
    # Coluna 'id' da tabela
    id = Column(Integer, primary_key=True, autoincrement=True, doc="Id da categoria")
    
    # Coluna 'name' da tabela
    name = Column(String(128), nullable=False, doc="Nome da categoria")
