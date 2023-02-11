from core.configs import settings
from core.database import engine
from sqlalchemy_utils import database_exists, create_database

async def create_table() -> None:
    import models.__all_models
    print('Criando as tabelas no banco de dados...')
    
    async with engine.begin() as conn:
        
        if not database_exists(settings.DB_URL):
            create_database(settings.DB_URL)
         
        await conn.run_sync(settings.DBBaseModel.metada.drop_all)
        await conn.run_sync(settings.DBBaseModel.metada.create_all)
    print('Tabelas Criadas com sucesso...')
    
    
if __name__ == '__main__':
    import asyncio
    
    asyncio.run(create_table())