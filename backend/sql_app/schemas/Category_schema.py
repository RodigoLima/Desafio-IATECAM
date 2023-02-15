# Importando o módulo "typing" e o tipo "Optional" dele
from typing import Optional

# Importando a classe "BaseModel" do módulo "pydantic"
from pydantic import BaseModel

 # Classe base de categoria que define os atributos básicos de um categoria
class CategoryBase(BaseModel):
    # Declarando uma variável de classe "id" 
    id: Optional[int]
    # Declarando uma variável de classe "name" 
    name: str

    class Config:
        orm_mode = True

# Classe que representa a requisição de uma categoria
class CategoryRequest(CategoryBase):
     # Herdando todos os atributos da classe CategoryBase
    ...

# Classe que representa a resposta de uma requisição de uma categoria
class CategoryResponse(CategoryBase):
    id: Optional[int]

    class Config:
        orm_mode = True
