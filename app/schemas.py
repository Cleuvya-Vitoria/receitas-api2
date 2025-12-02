# app/schemas.py
from sqlmodel import SQLModel, Field
from typing import List
from datetime import datetime


# =========================================
# USUARIO
# =========================================

class UsuarioCreate(SQLModel):
    nome: str
    email: str


class UsuarioRead(SQLModel):
    id: int
    nome: str
    email: str
    criado_em: datetime


# =========================================
# INGREDIENTE
# =========================================

class IngredienteCreate(SQLModel):
    nome: str
    unidade: str
    

class IngredienteRead(SQLModel):
    id: int
    nome: str
    unidade: str


# =========================================
# RECEITA
# =========================================

class ReceitaCreate(SQLModel):
    titulo: str
    descricao: str
    tempo_preparo_min: int
    nota_imdb: float
    usuario_id: int

class IngredienteDaReceita(SQLModel):
    id: int
    nome: str
    quantidade: float
    unidade: str

class ReceitaRead(SQLModel):
    id: int
    titulo: str
    descricao: str
    tempo_preparo_min: int 
    nota_imdb: float 
    criado_em: datetime
    usuario_id: int
    ingredientes: List[IngredienteDaReceita] = []




# =========================================
# RECEITA_INGREDIENTE
# =========================================

class ReceitaIngredienteCreate(SQLModel):
    receita_id: int
    ingrediente_id: int
    quantidade: float
    unidade: str


class ReceitaIngredienteRead(SQLModel):
    id: int
    receita_id: int
    ingrediente_id: int
    quantidade: float
    unidade: str