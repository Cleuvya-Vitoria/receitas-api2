# app/models/receita.py

from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .usuario import Usuario
    from .receita_ingrediente import ReceitaIngrediente


class Receita(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    titulo: str 
    descricao: str
    tempo_preparo_min: int = Field(default=None)
    nota_imdb: float = Field(default=None) 
    criado_em: datetime = Field(default_factory=datetime.utcnow)

    usuario_id: int = Field(foreign_key="usuario.id")

    usuarios: "Usuario" = Relationship(back_populates="receitas")

    ingredientes: List["ReceitaIngrediente"] = Relationship(
        back_populates="receita"
    )
    # ingredientes: List["Ingrediente"] = Relationship(back_populates="receita")