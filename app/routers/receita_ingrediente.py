# app/routers/receita_ingrediente.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.database import get_session
from app import crud
from app.schemas import ReceitaIngredienteCreate, ReceitaIngredienteRead

router = APIRouter(prefix="/receita-ingredientes", tags=["Receita-Ingrediente"])


@router.post("/", response_model=ReceitaIngredienteRead)
def adicionar_ingrediente(data: ReceitaIngredienteCreate, session: Session = Depends(get_session)):
    return crud.criar_receita_ingrediente(
        session,
        data.receita_id,
        data.ingrediente_id,
        data.quantidade,
        data.unidade
    )


@router.get("/receita/{receita_id}", response_model=list[ReceitaIngredienteRead])
def listar_ingredientes_da_receita(receita_id: int, session: Session = Depends(get_session)):
    return crud.listar_receita_ingredientes(session, receita_id)


@router.delete("/{assoc_id}")
def remover_assoc(assoc_id: int, session: Session = Depends(get_session)):
    ok = crud.remover_ingrediente_de_receita(session, assoc_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Associação não encontrada")
    return {"mensagem": "Associação removida"}