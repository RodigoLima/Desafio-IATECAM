# Importa a função Session do módulo sqlalchemy.orm
from sqlalchemy.orm import Session

# Importa a função HTTPException e status do módulo fastapi
from fastapi import  HTTPException,status

# Importa o modelo de Produto
from models.Product_model import Product

class ProductRepository:

    
    @staticmethod
    def verifica_nroserie(serie: int):
        if serie <= 0:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="O campo série só permitido números positivos." )
    
    # Método que retorna uma lista de todos os produtos no banco de dados   
    @staticmethod
    def find_all(session: Session) -> list[Product]:
        # Retorna todos os objetos de produto na tabela do banco de dados
        return session.query(Product).all()

    # Método que adiciona um novo produto ao banco de dados
    @staticmethod
    def save(session: Session, product: Product) -> Product:
        
        # Verifica se o número de série é positivo
        ProductRepository.verifica_nroserie(product.serie)
        
        # Verifição de preenchimento de todos os campos 
        if not all([product.name, product.category, product.price, product.serie]):
            raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Todos os campos são obrigatórios."
        )
        # Adiciona o produto ao banco de dados
        session.add(product)
        # Salva as alterações no banco de dados
        session.commit()
        # Retorna o produto adicionado
        return product

    # Método que atualiza as informações de um produto existente no banco de dados
    @staticmethod
    def update(session: Session, product: Product,id: int) -> Product:
        
        # Verifica se o número de série é positivo
        ProductRepository.verifica_nroserie(product.serie)
        
        # Busca o produto pelo id
        product_up = session.query(Product).filter(Product.id == id).first()
        # Atualiza as informações do produto
        product_up.name = product.name
        product_up.category = product.category
        product_up.price = product.price
        product_up.serie = product.serie
        # Mescla as alterações no banco de dados
        session.merge(product_up)
        # Salva as alterações no banco de dados
        session.commit()
        # Retorna o produto atualizado
        return product_up

    # Método que retorna um produto específico pelo id
    @staticmethod
    def find_by_id(session: Session, id: int) -> Product:
        # Retorna o primeiro produto encontrado com o id especificado
        return session.query(Product).filter(Product.id == id).first()

    # Método que verifica se um produto com o id especificado existe no banco de dados
    @staticmethod
    def exists_by_id(session: Session, id: int) -> bool:
        # Retorna verdadeiro se o produto existe e falso caso contrário
        return session.query(Product).filter(Product.id == id).first() is not None

    # Método que remove um produto existente do banco de dados
    @staticmethod
    def delete_by_id(session: Session, id: int) -> None:
        # Busca o produto pelo id
        product = session.query(Product).filter(Product.id == id).first()
        # Verifica se o produto existe
        if product is not None:
            # Remove o produto do banco de dados
            session.delete(product)
            # Salva as alterações no banco de dados
            session.commit()
