from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    # Configurações Gerais Usadas na API
    
    API_V1_STR: str = "/api/v1" # versão da api
    DB_URL: str = "mysql+mysqlconnector://root:123@localhost:3306/desafioiatecam" 
    DBBaseModel = declarative_base()
    
    class Config:
        case_sensitive = True
        
        
settings = Settings()