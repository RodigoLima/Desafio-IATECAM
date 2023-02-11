# Importa a função create_engine do módulo sqlalchemy
from sqlalchemy import create_engine,exc

# Importa a classe declarative_base do módulo sqlalchemy.ext.declarative
from sqlalchemy.ext.declarative import declarative_base

# Importa a função sessionmaker do módulo sqlalchemy.orm
from sqlalchemy.orm import sessionmaker

# Define a variável de ambiente SQLALCHEMY_DATABASE_URL, que contém a string de conexão com o banco de dados
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:123@localhost:3306/desafioiatecam"

# Cria uma instância da classe Engine usando a função create_engine e a string de conexão fornecida na variável SQLALCHEMY_DATABASE_URL
try:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
except exc.SQLAlchemyError as e:
    # Trata o erro e imprime a mensagem de erro
    print("Erro ao criar a instância do Engine: ", e)

# Cria uma instância da classe sessionmaker com as opções autocommit e autoflush definidas como False e a instância engine para fazer a ligação
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma instância da classe declarative_base
Base = declarative_base()

# Define a função get_db, que cria uma sessão local e a retorna para o chamador
def get_db():
    try:
        # Cria uma sessão local
        db = SessionLocal()
    except exc.SQLAlchemyError as e:
        # Trata o erro e imprime a mensagem de erro
        print("Erro ao criar a sessão local: ", e)
    
    try:
        # Retorna a sessão local para o chamador
        yield db
    finally:
        try:
            # Fecha a sessão local ao final da execução, garantindo a liberação de recursos
            db.close()
        except exc.SQLAlchemyError as e:
            # Trata o erro e imprime a mensagem de erro
            print("Erro ao fechar a sessão local")