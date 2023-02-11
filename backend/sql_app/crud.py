from sqlalchemy.orm import Session

import models, schemas

def get_categorys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def get_category(db: Session, id_get: int):
    return db.query(models.Category).filter(models.Category.id == id_get).first()


def create_category(db: Session, category: schemas.Category):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, id_put:int , category_put: schemas.Category):
    db_category = db.query(models.Category).filter(models.Category.id == id_put).first()
    db_category.update("name=teste")
    return db_category