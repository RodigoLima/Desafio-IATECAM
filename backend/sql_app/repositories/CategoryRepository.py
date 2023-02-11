from sqlalchemy.orm import Session

from models import Category

class CategoryRepository:
    @staticmethod
    def find_all(db: Session) -> list[Category]:
        return db.query(Category).all()

    @staticmethod
    def save(db: Session, category: Category) -> Category:
        if category.id:
            db.merge(category)
        else:
            db.add(category)
        db.commit()
        return category

    @staticmethod
    def find_by_id(db: Session, id: int) -> Category:
        return db.query(Category).filter(Category.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Category).filter(Category.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        category = db.query(Category).filter(Category.id == id).first()
        if category is not None:
            db.delete(category)
            db.commit()