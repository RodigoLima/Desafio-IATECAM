from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models.Category_model import Category
from models.Product_model import Product
from core.database import engine, Base, get_db
from repositories.CategoryRepository import CategoryRepository
from repositories.ProductRepository import ProductRepository
from schemas.Category_schema import CategoryRequest, CategoryResponse
from schemas.Product_schema import ProductRequest, ProductResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/api/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create(request: ProductRequest, db: Session = Depends(get_db)):
    products = ProductRepository.save(db, Product(**request.dict()))
    return ProductResponse.from_orm(products)

@app.get("/api/products", response_model=list[ProductResponse])
def find_all(db: Session = Depends(get_db)):
    products = ProductRepository.find_all(db)
    return [ProductResponse.from_orm(product) for product in products]

@app.get("/api/products/{id}", response_model=ProductResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    product = ProductRepository.find_by_id(db, id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    return ProductResponse.from_orm(product)

@app.delete("/api/products/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not ProductRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    ProductRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/products/{id}", response_model=ProductResponse)
def update(id: int, request: ProductRequest, db: Session = Depends(get_db)):
    if not ProductRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    product = ProductRepository.update(db, Product(**request.dict()),id)
    return ProductResponse.from_orm(product)


#------------------------------------------------------------------------- CRUD CATEGORY --------------------------------------#
@app.post("/api/categories", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create(request: CategoryRequest, db: Session = Depends(get_db)):
    category = CategoryRepository.save(db, Category(**request.dict()))
    return CategoryResponse.from_orm(category)


@app.get("/api/categories", response_model=list[CategoryResponse])
def find_all(db: Session = Depends(get_db)):
    categories = CategoryRepository.find_all(db)
    return [CategoryResponse.from_orm(category) for category in categories]

@app.get("/api/categories/{id}", response_model=CategoryResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    category = CategoryRepository.find_by_id(db, id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )
    return CategoryResponse.from_orm(category)

@app.delete("/api/categories/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not CategoryRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )
    CategoryRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/categories/{id}", response_model=CategoryResponse)
def update(id: int, request: CategoryRequest, db: Session = Depends(get_db)):
    if not CategoryRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )
    category = CategoryRepository.update(db, Category(**request.dict()),id)
    return CategoryResponse.from_orm(category)