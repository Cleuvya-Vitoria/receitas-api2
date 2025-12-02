# app/database.py
from sqlmodel import SQLModel, create_engine, Session
import os
from typing import Generator
from sqlalchemy.engine import Engine
from dotenv import load_dotenv


# Carrega variáveis do .env
# load_dotenv()  # procura por um arquivo .env na raiz do projeto

# # LER A URL DO .env: aconselho usar python-dotenv em produção/no dev
DATABASE_URL = "sqlite:///database.db"

# Agora você pode usar os valores do .env
# DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")


# Cria engine para SQLModel (funciona com SQLite e PostgreSQL)
engine: Engine = create_engine(
    DATABASE_URL,
    echo=True)
    # connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
    # )

def get_engine() -> Engine:
    """Retorna a engine usada pelo SQLModel e pelo Alembic."""
    return engine

def criar_tabelas():
    """
    Apenas para desenvolvimento: cria todas as tabelas via SQLModel.metadata.
    Em produção devemos usar Alembic (migrations) - não rodar isso no deploy.
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """
    Dependência geradora para injeção de sessão no FastAPI.
    Uso típico: with next(get_session()) as session: ...
    No FastAPI, usar Depends(get_session).
    """
    with Session(engine) as session:
        yield session