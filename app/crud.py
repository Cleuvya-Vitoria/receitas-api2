# app/crud.py
from sqlmodel import Session, select
from sqlalchemy.orm import joinedload, selectinload
from app.models import Usuario, Ingrediente, Receita, ReceitaIngrediente
from sqlalchemy import extract


# =========================================================
# USUÁRIO CRUD
# =========================================================

def criar_usuario(session: Session, nome: str, email: str):
    usuario = Usuario(nome=nome, email=email)
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


def obter_usuario_por_id(session: Session, usuario_id: int):
    return session.get(Usuario, usuario_id)


def listar_usuarios(session: Session, offset: int = 0, limit: int = 10):
    query = select(Usuario).offset(offset).limit(limit)
    return session.exec(query).all()


def atualizar_usuario(session: Session, usuario_id: int, nome: str, email: str):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        return None
    usuario.nome = nome
    usuario.email = email
    session.commit()
    session.refresh(usuario)
    return usuario


def excluir_usuario(session: Session, usuario_id: int):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        return False
    session.delete(usuario)
    session.commit()
    return True


# =========================================================
# INGREDIENTE CRUD
# =========================================================

def criar_ingrediente(session: Session, nome: str, unidade: str):
    ingrediente = Ingrediente(nome=nome, unidade=unidade)
    session.add(ingrediente)
    session.commit()
    session.refresh(ingrediente)
    return ingrediente


def obter_ingrediente_por_id(session: Session, ingrediente_id: int):
    return session.get(Ingrediente, ingrediente_id)


def listar_ingredientes(session: Session, offset: int = 0, limit: int = 10):
    query = select(Ingrediente).offset(offset).limit(limit)
    return session.exec(query).all()


def atualizar_ingrediente(session: Session, ingrediente_id: int, nome: str, unidade: str):
    ingrediente = session.get(Ingrediente, ingrediente_id)
    if not ingrediente:
        return None
    ingrediente.nome = nome
    ingrediente.unidade = unidade
    session.commit()
    session.refresh(ingrediente)
    return ingrediente


def excluir_ingrediente(session: Session, ingrediente_id: int):
    ingrediente = session.get(Ingrediente, ingrediente_id)
    if not ingrediente:
        return False
    session.delete(ingrediente)
    session.commit()
    return True


# =========================================================
# RECEITA CRUD
# =========================================================

def criar_receita(session: Session, titulo: str, descricao: str, tempo_preparo_min: int, nota_imdb: float, usuario_id: int):
    receita = Receita(
        titulo=titulo,
        descricao=descricao,
        tempo_preparo_min=tempo_preparo_min,
        nota_imdb=nota_imdb,
        usuario_id=usuario_id
    )
    session.add(receita)
    session.commit()
    session.refresh(receita)
    return receita


def obter_receita_por_id(session: Session, receita_id: int):
    query = (
        select(Receita)
        .where(Receita.id == receita_id)
        .options(
            joinedload(Receita.ingredientes).joinedload(ReceitaIngrediente.ingrediente)
        )
        .distinct()  # garante que a receita não se repita na saída
    )
    return session.exec(query).first()




# def listar_receitas(session: Session, ano: int = None, offset: int = 0, limit: int = 10):
#     query = select(Receita)

#     if ano is not None:
#         # filtra pelo ano usando SQL
#         query = query.where(extract('year',Receita.criado_em) == ano)

#     query = query.offset(offset).limit(limit)
#     return session.exec(query).all()

def listar_receitas(session: Session, ano: int | None = None, offset: int = 0, limit: int = 10):

    query = (
        select(Receita)
        # carrega lista de ReceitaIngrediente
        .options(
            selectinload(Receita.ingredientes)
            # e dentro de cada ReceitaIngrediente, carrega o Ingrediente
            .selectinload(ReceitaIngrediente.ingrediente)
        )
    )

    if ano is not None:
        query = query.where(extract("year", Receita.criado_em) == ano)

    query = query.offset(offset).limit(limit)

    return session.exec(query).all()


def atualizar_receita(session: Session, receita_id: int, **dados):
    receita = session.get(Receita, receita_id)
    if not receita:
        return None

    for campo, valor in dados.items():
        setattr(receita, campo, valor)

    session.commit()
    session.refresh(receita)
    return receita


def excluir_receita(session: Session, receita_id: int):
    receita = session.get(Receita, receita_id)
    if not receita:
        return False
    session.delete(receita)
    session.commit()
    return True


# =========================================================
# RECEITA_INGREDIENTE CRUD
# =========================================================

def criar_receita_ingrediente(session: Session, receita_id: int, ingrediente_id: int, quantidade: float, unidade: str):
    ri = ReceitaIngrediente(
        receita_id=receita_id,
        ingrediente_id=ingrediente_id,
        quantidade=quantidade,
        unidade=unidade
    )
    session.add(ri)
    session.commit()
    session.refresh(ri)
    return ri


def listar_receita_ingredientes(session: Session, receita_id: int):
    query = select(ReceitaIngrediente).where(ReceitaIngrediente.receita_id == receita_id)
    return session.exec(query).all()


def excluir_receita_ingrediente(session: Session, ri_id: int):
    ri = session.get(ReceitaIngrediente, ri_id)
    if not ri:
        return False
    session.delete(ri)
    session.commit()
    return True