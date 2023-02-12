# Importa os pacotes e módulos necessários
from fastapi import APIRouter
from fastapi import  Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from models.Category_model import Category # Importa o modelo Category
from validacoes.CategoryValidacao import CategoryValidacao # Importa a classe de validação CategoryValidacao
from core.database import engine, Base, get_db # Importa o engine do banco de dados e a função get_db para obter uma sessão
from repositories.CategoryRepository import CategoryRepository # Importa o repositório CategoryRepository
from schemas.Category_schema import CategoryRequest, CategoryResponse # Importa os esquemas CategoryRequest e CategoryResponse

# Cria uma instância de APIRouter para definir as rotas da API
router = APIRouter()

# Rota do endpoint para criar uma categoria
@router.post("/api/categories/createcategory", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create(request: CategoryRequest, db: Session = Depends(get_db)):
    # Validação da categoria antes de salvar no banco de dados
    CategoryValidacao.vfr_all(Category(**request.dict()),db)
    # Salva a categoria no banco de dados
    category = CategoryRepository.save(db, Category(**request.dict()))
    # Retorna a categoria criada
    return CategoryResponse.from_orm(category)

# Rota do endpoint que retorna todas as categorias
@router.get("/api/categories/getallCategory", response_model=list[CategoryResponse])
def find_all(db: Session = Depends(get_db)):
    # Busca por todas as categorias no banco de dados
    categories = CategoryRepository.find_all(db)
    # Transforma as categorias encontradas em objetos CategoryResponse
    return [CategoryResponse.from_orm(category) for category in categories]

# Rota do endpoint que retorna uma categoria pelo ID
@router.get("/api/categories/getcategorybyid/{id}", response_model=CategoryResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    # Obtem a categoria através de um ID
    category = CategoryRepository.find_by_id(db, id)
    
    # Se a categoria não for encontrada, uma exceção HTTP é gerada
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )
        
    # Retorna a categoria como uma resposta
    return CategoryResponse.from_orm(category)

# Rotas do endpoint para deletar uma categoria pelo ID
@router.delete("/api/categories/deletecategorybyid/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    # Verifica se a categoria com o ID especificado existe na base de dados
    if not CategoryRepository.exists_by_id(db, id):
        # Caso não exista, uma exceção HTTP é gerada
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )
    # Se a categoria existir, ela é deletada da base de dados
    CategoryRepository.delete_by_id(db, id)
    # Uma resposta vazia é retornada, indicando que a operação de deletar a categoria foi realizada com sucesso
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Rotas do endpoint para atualizar uma categoria pelo ID
@router.put("/api/categories/updatecategorybyid/{id}", response_model=CategoryResponse)
def update(id: int, request: CategoryRequest, db: Session = Depends(get_db)):
    # Valida os dados da categoria
    CategoryValidacao.vfr_all(Category(**request.dict()),db)

    # Verifica se a categoria existe
    if not CategoryRepository.exists_by_id(db, id):
        # Caso não exista, levanta um erro HTTP 404 (Not Found)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )
    
    # Atualiza a categoria
    category = CategoryRepository.update(db, Category(**request.dict()),id)

    # Retorna a categoria atualizada
    return CategoryResponse.from_orm(category)