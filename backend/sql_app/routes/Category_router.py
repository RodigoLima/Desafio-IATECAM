
from fastapi import APIRouter
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from models.Category_model import Category
from validacoes.CategoryValidacao import CategoryValidacao
from core.database import engine, Base, get_db
from repositories.CategoryRepository import CategoryRepository
from schemas.Category_schema import CategoryRequest, CategoryResponse


router = APIRouter()


@router.post("/api/categories", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create(request: CategoryRequest, db: Session = Depends(get_db)):
    CategoryValidacao.vfr_all(Category(**request.dict()),db)
    category = CategoryRepository.save(db, Category(**request.dict()))
    return CategoryResponse.from_orm(category)

@router.get("/api/categories", response_model=list[CategoryResponse])
def find_all(db: Session = Depends(get_db)):
    categories = CategoryRepository.find_all(db)
    return [CategoryResponse.from_orm(category) for category in categories]

@router.get("/api/categories/{id}", response_model=CategoryResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    category = CategoryRepository.find_by_id(db, id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )
    return CategoryResponse.from_orm(category)

@router.delete("/api/categories/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not CategoryRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )
    CategoryRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/api/categories/{id}", response_model=CategoryResponse)
def update(id: int, request: CategoryRequest, db: Session = Depends(get_db)):
    CategoryValidacao.vfr_all(Category(**request.dict()),db)
    if not CategoryRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )
    category = CategoryRepository.update(db, Category(**request.dict()),id)
    return CategoryResponse.from_orm(category)