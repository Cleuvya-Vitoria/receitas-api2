# app/models/ingrediente.py
from typing import List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .receita_ingrediente import ReceitaIngrediente

class Ingrediente(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    # id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(...)
    unidade: str | None = Field(None)  # unidade padrão do ingrediente
    # quantidade: int     # em ml, em gramas

    receitas: List["ReceitaIngrediente"] = Relationship(
        back_populates="ingrediente"
    )
