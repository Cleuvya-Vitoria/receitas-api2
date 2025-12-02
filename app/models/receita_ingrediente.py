# app/models/receita_ingrediente.py

from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .receita import Receita
    from .ingrediente import Ingrediente


class ReceitaIngrediente(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    receita_id: int = Field(..., foreign_key="receita.id")
    ingrediente_id: int = Field(..., foreign_key="ingrediente.id")

    quantidade: float = Field(...)
    unidade: str = Field(...)

    receita: "Receita" = Relationship(back_populates="ingredientes")
    ingrediente: "Ingrediente" = Relationship(back_populates="receitas")