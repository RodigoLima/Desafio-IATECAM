# Importa a função Session do módulo sqlalchemy.orm
from sqlalchemy.orm import Session

# Importa o modelo da categoria
from models.Category_model import Category

# Classe do repositório da categoria
class CategoryRepository:
    # Método para encontrar todas as categorias
    @staticmethod
    def find_all(session: Session) -> list[Category]:
        # Retorna uma lista de todos os objetos da categoria na sessão do banco de dados
        return session.query(Category).all()

    # Método para salvar uma categoria
    @staticmethod
    def save(session: Session, category: Category) -> Category:
        # Adiciona a categoria à sessão
        session.add(category)
        # Efetua o commit na sessão para salvar a categoria no banco de dados
        session.commit()
        # Retorna a categoria salva
        return category

    # Método para atualizar uma categoria
    @staticmethod
    def update(session: Session, category: Category,id: int) -> Category:
        # Encontra a categoria a ser atualizada com o id especificado
        category_up = session.query(Category).filter(Category.id == id).first()
        # Atualiza o nome da categoria
        category_up.name = category.name
        # Mescla a categoria atualizada com a sessão do banco de dados
        session.merge(category_up)
        # Efetua o commit na sessão para salvar a categoria atualizada no banco de dados
        session.commit()
        # Retorna a categoria atualizada
        return category_up

    # Método para encontrar uma categoria por id
    @staticmethod
    def find_by_id(session: Session, id: int) -> Category:
        # Retorna a categoria encontrada com o id especificado
        return session.query(Category).filter(Category.id == id).first()

    # Método para verificar se uma categoria existe por id
    @staticmethod
    def exists_by_id(session: Session, id: int) -> bool:
        # Retorna verdadeiro se uma categoria com o id especificado existir, caso contrário, retorna falso
        return session.query(Category).filter(Category.id == id).first() is not None

    # Método para excluir uma categoria por id
    @staticmethod
    def delete_by_id(session: Session, id: int) -> None:
        # Encontra a categoria com o id especificado
        category = session.query(Category).filter(Category.id == id).first()
        # Se a categoria existir, exclui a categoria da sessão do banco de dados
        if category is not None:
            session.delete(category)
            session.commit()
