# app/routers/ingredientes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.database import get_session
from app import crud
from app.schemas import IngredienteCreate, IngredienteRead

router = APIRouter(prefix="/ingredientes", tags=["Ingredientes"])


@router.post("/", response_model=IngredienteRead)
def criar_ingrediente(ingrediente: IngredienteCreate, session: Session = Depends(get_session)):
    return crud.criar_ingrediente(session, ingrediente.nome, ingrediente.unidade)


@router.get("/{ingrediente_id}", response_model=IngredienteRead)
def obter_ingrediente(ingrediente_id: int, session: Session = Depends(get_session)):
    ing = crud.obter_ingrediente_por_id(session, ingrediente_id)
    if not ing:
        raise HTTPException(status_code=404, detail="Ingrediente não encontrado")
    return ing


# @router.get("/", response_model=list[IngredienteRead])
# def listar_ingredientes(filtro_nome: str = None, session: Session = Depends(get_session)):
#     return crud.listar_ingredientes(session, filtro_nome)
@router.get("/", response_model=list[IngredienteRead])
def listar_ingredientes(
    # Dependência de Sessão
    session: Session = Depends(get_session),
    
    # Parâmetros de Paginação
    offset: int = 0, # Número de registros a pular (offset)
    limit: int = 10 # Número máximo de registros a retornar
):
    """
    Lista todos os ingredientes com suporte à paginação.
    
    - 'offset' (int): Quantos itens pular
    - 'limit' (int): Quantos itens retornar (máx. 10).
    """
    
    # Chama a função CRUD, passando a sessão, o skip (offset) e o limit
    # Presumimos que crud.listar_ingredientes foi atualizada para aceitar 'skip' e 'limit'
    return crud.listar_ingredientes(session, offset=offset, limit=limit)



@router.put("/{ingrediente_id}", response_model=IngredienteRead)
def atualizar_ingrediente(ingrediente_id: int, ingrediente: IngredienteCreate, session: Session = Depends(get_session)):
    ing = crud.atualizar_ingrediente(session, ingrediente_id, nome=ingrediente.nome, unidade=ingrediente.unidade)
    if not ing:
        raise HTTPException(status_code=404, detail="Ingrediente não encontrado")
    return ing


@router.delete("/{ingrediente_id}")
def excluir_ingrediente(ingrediente_id: int, session: Session = Depends(get_session)):
    ok = crud.excluir_ingrediente(session, ingrediente_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Ingrediente não encontrado")
    return {"mensagem": "Ingrediente excluído com sucesso"}