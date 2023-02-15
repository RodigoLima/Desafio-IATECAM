from fastapi import  HTTPException,status,Depends
from models.Category_model import Category
from repositories.ProductRepository import ProductRepository
from sqlalchemy.orm import Session
from core.database import engine, Base, get_db

class CategoryValidacao:
    
    # Verifição de preenchimento de todos os campos 
    def vrf_campos_obrigatorios(category: Category):
        if not all([category.name]):
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Todos os campos são obrigatórios.")
    
    def vrf_category_product_exists(id: int, db: Session = Depends(get_db)):
        product = ProductRepository.find_by_id_category_produt(db, id)
        if product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="O id da categoria não pode ser deletado pois está vinculado a um produto."
            )    
        
    # Verifica o tamanho do nome da categoria
    def vrf_name_category(name: str):
        if len(name) > 128:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nome da categoria excedeu o tamanho máximo de 128 carecteres.")
    
    # Verificao geral 
    def vfr_all(category: Category,db):
        CategoryValidacao.vrf_name_category(category.name)
        CategoryValidacao.vrf_campos_obrigatorios(category)