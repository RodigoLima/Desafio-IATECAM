from fastapi import  Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from validacoes.ProductValidacao import ProductValidacao
from fastapi import APIRouter
from models.Product_model import Product
from core.database import engine, Base, get_db
from repositories.ProductRepository import ProductRepository
from schemas.Product_schema import ProductRequest, ProductResponse


# Cria uma instância de APIRouter para definir as rotas da API
router = APIRouter()

# Rota do endpoint para criar um produto
@router.post("/api/products/createproduct", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create(request: ProductRequest, db: Session = Depends(get_db)):
    # Valida os dados do produto antes de salvar no banco
    ProductValidacao.vfr_all(Product(**request.dict()), db)
    # Salva o produto no banco de dados
    products = ProductRepository.save(db, Product(**request.dict()))
    # Retorna o produto salvo
    return ProductResponse.from_orm(products)

# Rota para listar todos os produtos
@router.get("/api/products/getallproduct", response_model=list[ProductResponse])
def find_all(db: Session = Depends(get_db)):
    # Busca todos os produtos no banco de dados
    products = ProductRepository.find_all(db)
    # Retorna a lista de todos os produtos
    return [ProductResponse.from_orm(product) for product in products]

# Rota do endpoint que retorna um produto pelo ID
@router.get("/api/products/getproductbyid/{id}", response_model=ProductResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    # Busca um produto no banco de dados pelo ID
    product = ProductRepository.find_by_id(db, id)
    # Se o produto não for encontrado, retorna erro 404
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    # Retorna o produto encontrado
    return ProductResponse.from_orm(product)

# Rotas do endpoint para deletar uma produto pelo ID
@router.delete("/api/products/deleteproductbyid/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    # Verifica se o produto existe antes de deletar
    if not ProductRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    # Deleta o produto do banco de dados
    ProductRepository.delete_by_id(db, id)

# Rotas do endpoint para atualizar um produto pelo ID
@router.put("/api/products/updateproductbyid/{id}", response_model=ProductResponse)
def update(id: int, request: ProductRequest, db: Session = Depends(get_db)):
    # Realiza as validações no objeto produto
    ProductValidacao.vfr_all(Product(**request.dict()),db)
    
    # Verifica se o produto existe no banco de dados
    if not ProductRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
        
    # Atualiza o produto no banco de dados
    product = ProductRepository.update(db, Product(**request.dict()),id)
    
    # Retorna a resposta do produto atualizado
    return ProductResponse.from_orm(product)