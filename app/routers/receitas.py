# app/routers/receitas.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from datetime import datetime
from sqlalchemy import select, extract

from app.schemas import IngredienteDaReceita, ReceitaRead
from app.database import get_session
from app import crud
from app.schemas import ReceitaCreate, ReceitaRead

router = APIRouter(prefix="/receitas", tags=["Receitas"])


@router.post("/", response_model=ReceitaRead)
def criar_receita(receita: ReceitaCreate, session: Session = Depends(get_session)):
    return crud.criar_receita(
        session,
        titulo=receita.titulo,
        descricao=receita.descricao,
        tempo_preparo_min=receita.tempo_preparo_min,
        nota_imdb=receita.nota_imdb,
        usuario_id=receita.usuario_id
    )


@router.get("/{receita_id}", response_model=ReceitaRead)
def obter_receita(receita_id: int, session: Session = Depends(get_session)):
    r = crud.obter_receita_por_id(session, receita_id)
    if not r:
        raise HTTPException(status_code=404, detail="Receita não encontrada")

    ingredientes = [
        IngredienteDaReceita(
            id=ri.ingrediente.id,
            nome=ri.ingrediente.nome,
            quantidade=ri.quantidade,
            unidade=ri.unidade
        )
        for ri in r.ingredientes
    ]

    return ReceitaRead(
        id=r.id,
        titulo=r.titulo,
        descricao=r.descricao,
        tempo_preparo_min=r.tempo_preparo_min,
        nota_imdb=r.nota_imdb,
        criado_em=r.criado_em,
        usuario_id=r.usuario_id,
        ingredientes=ingredientes
    )


# @router.get("/", response_model=list[ReceitaRead])
# def listar_receitas(
#     ano: int = None,
#     offset: int = 0,
#     limit: int = 10,
#     session: Session = Depends(get_session)
# ):
#     receitas = listar_receitas(session=session, ano=ano, offset=offset, limit=limit)
#     return [ReceitaRead.model_validate(r) for r in receitas]
    
@router.get("/", response_model=list[ReceitaRead])
def listar_receitas_endpoint(
    ano: int = None,
    offset: int = 0,
    limit: int = 10,
    session: Session = Depends(get_session)
):
    receitas = crud.listar_receitas(session, ano, offset, limit)

    resposta = []
    for r in receitas:
        ingredientes = [
            IngredienteDaReceita(
                id=ri.ingrediente.id,
                nome=ri.ingrediente.nome,
                quantidade=ri.quantidade,
                unidade=ri.unidade
            )
            for ri in r.ingredientes
        ]

        resposta.append(
            ReceitaRead(
                id=r.id,
                titulo=r.titulo,
                descricao=r.descricao,
                tempo_preparo_min=r.tempo_preparo_min,
                nota_imdb=r.nota_imdb,
                criado_em=r.criado_em,
                usuario_id=r.usuario_id,
                ingredientes=ingredientes
            )
        )

    return resposta


@router.put("/{receita_id}", response_model=ReceitaRead)
def atualizar_receita(receita_id: int, receita: ReceitaCreate, session: Session = Depends(get_session)):
    r = crud.atualizar_receita(session, receita_id, receita.titulo, receita.descricao, receita.tempo_preparo_min, receita.nota_imdb)
    if not r:
        raise HTTPException(status_code=404, detail="Receita não encontrada")
    return r


@router.delete("/{receita_id}")
def excluir_receita(receita_id: int, session: Session = Depends(get_session)):
    ok = crud.excluir_receita(session, receita_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Receita não encontrada")
    return {"mensagem": "Receita excluída"}