# app/models/usuario.py

from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .receita import Receita


class UsuarioBase(SQLModel):
    nome: str = Field(...)
    email: str = Field(..., index=True)


class Usuario(UsuarioBase, table=True):
    id: int = Field(default=None, primary_key=True)
    criado_em: datetime = Field(default_factory=datetime.utcnow)

    receitas: List["Receita"] = Relationship(back_populates="usuarios")