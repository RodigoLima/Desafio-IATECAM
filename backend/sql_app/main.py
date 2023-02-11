from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/categorys/", response_model=list[schemas.Category])  #GET ALL CATEGORIAS
def read_categorys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorys = crud.get_categorys(db, skip=skip, limit=limit)
    return categorys

@app.get("/categorys/{id_category}", response_model=schemas.Category) # GET ID CATEGORIA
def read_category(id_category: int, db: Session = Depends(get_db)):
    db_user = crud.get_category(db, id_get=id_category)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada...")
    return db_user

@app.post("/categorys/", response_model=schemas.Category)  #
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

@app.post("/categorys/{id_category}", response_model=schemas.Category)
def update_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)
