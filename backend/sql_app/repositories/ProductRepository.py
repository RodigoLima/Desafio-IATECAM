from sqlalchemy.orm import Session

from models.Product_model import Product

class ProductRepository:
    @staticmethod
    def find_all(db: Session) -> list[Product]:
        return db.query(Product).all()

    @staticmethod
    def save(db: Session, product: Product) -> Product:
        db.add(product)
        db.commit()
        return product

    @staticmethod
    def update(db: Session, product: Product,id: int) -> Product:
        product_up = db.query(Product).filter(Product.id == id).first()
        product_up.name = product.name
        db.merge(product_up)
        db.commit()
        return product_up

    @staticmethod
    def find_by_id(db: Session, id: int) -> Product:
        return db.query(Product).filter(Product.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Product).filter(Product.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        product = db.query(Product).filter(Product.id == id).first()
        if product is not None:
            db.delete(product)
            db.commit()