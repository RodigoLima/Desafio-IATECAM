# Importa a função HTTPException e status do módulo fastapi
from fastapi import  HTTPException,status,Depends
# Importa o modelo de Produto
from models.Product_model import Product
from core.database import engine, Base, get_db

from sqlalchemy.orm import Session
from repositories.CategoryRepository import CategoryRepository

class ProductValidacao:
     
    # Verifição de preenchimento de todos os campos 
    def vrf_campos_obrigatorios(product: Product):
        if not all([product.name, product.category, product.price, product.serie]):
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Todos os campos são obrigatórios."
        )
    
    # Verifica se o id da categoria do produto existe  
    def vrf_category_exists(id: int, db: Session = Depends(get_db)):
        category = CategoryRepository.find_by_id(db, id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="O id da categoria do produto não existe."
            )
            
    # Verifica se o numero de serie do produto é positivo
    def vrf_nroserie(serie: int):
        if serie <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="O campo série só é permitido números positivos." )
    
    # Verifica o tamanho do nome do produto
    def vrf_name_category(name: str):
        if len(name) > 60:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nome do Produto excedeu o tamanho máximo de 60 carecteres.")

    #verificacao geral 
    def vfr_all(product: Product,db):
        ProductValidacao.vrf_campos_obrigatorios(product)
        ProductValidacao.vrf_nroserie(product.serie)
        ProductValidacao.vrf_name_category(product.name)
        ProductValidacao.vrf_category_exists(product.category,db)