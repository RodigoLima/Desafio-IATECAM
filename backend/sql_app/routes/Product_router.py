from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from validacoes.ProductValidacao import ProductValidacao
from fastapi import APIRouter
from models.Category_model import Category
from models.Product_model import Product
from core.database import engine, Base, get_db
from repositories.CategoryRepository import CategoryRepository
from repositories.ProductRepository import ProductRepository
from schemas.Category_schema import CategoryRequest, CategoryResponse
from schemas.Product_schema import ProductRequest, ProductResponse


router = APIRouter()

@router.post("/api/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create(request: ProductRequest, db: Session = Depends(get_db)):
    ProductValidacao.vfr_all(Product(**request.dict()),db)
    products = ProductRepository.save(db, Product(**request.dict()))
    return ProductResponse.from_orm(products)

@router.get("/api/products", response_model=list[ProductResponse])
def find_all(db: Session = Depends(get_db)):
    products = ProductRepository.find_all(db)
    return [ProductResponse.from_orm(product) for product in products]

@router.get("/api/products/{id}", response_model=ProductResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    product = ProductRepository.find_by_id(db, id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    return ProductResponse.from_orm(product)

@router.delete("/api/products/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not ProductRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    ProductRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/api/products/{id}", response_model=ProductResponse)
def update(id: int, request: ProductRequest, db: Session = Depends(get_db)):
    ProductValidacao.vfr_all(Product(**request.dict()),db)
    if not ProductRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    product = ProductRepository.update(db, Product(**request.dict()),id)
    return ProductResponse.from_orm(product)