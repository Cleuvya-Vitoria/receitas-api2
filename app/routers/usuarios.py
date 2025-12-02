# app/routers/usuarios.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.database import get_session
from app import crud
from app.schemas import UsuarioCreate, UsuarioRead

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("/", response_model=UsuarioRead)
def criar_usuario(usuario: UsuarioCreate, session: Session = Depends(get_session)):
    return crud.criar_usuario(session, usuario.nome, usuario.email)


@router.get("/{usuario_id}", response_model=UsuarioRead)
def obter_usuario(usuario_id: int, session: Session = Depends(get_session)):
    usuario = crud.obter_usuario_por_id(session, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


@router.get("/", response_model=list[UsuarioRead])
def listar_usuarios(offset: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    return crud.listar_usuarios(session, offset, limit)


@router.put("/{usuario_id}", response_model=UsuarioRead)
def atualizar_usuario(usuario_id: int, usuario: UsuarioCreate, session: Session = Depends(get_session)):
    atualizado = crud.atualizar_usuario(session, usuario_id, nome=usuario.nome, email=usuario.email)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return atualizado


@router.delete("/{usuario_id}")
def excluir_usuario(usuario_id: int, session: Session = Depends(get_session)):
    ok = crud.excluir_usuario(session, usuario_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"mensagem": "Usuário excluído com sucesso"}