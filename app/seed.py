from sqlmodel import Session
from app.database import get_engine
from app.models.usuario import Usuario
from app.models.receita import Receita
from app.models.ingrediente import Ingrediente
from app.models.receita_ingrediente import ReceitaIngrediente


def popular_banco():
    engine = get_engine()

    with Session(engine) as session:

        # ===========================
        #   USUÁRIOS (10 instâncias)
        # ===========================
        usuarios = [
            Usuario(nome="Ana", email="ana@email"),
            Usuario(nome="Bruno", email="bruno@email"),
            Usuario(nome="Carla", email="carla@email"),
            Usuario(nome="Daniel", email="daniel@email"),
            Usuario(nome="Eduarda", email="eduarda@email"),
            Usuario(nome="Felipe", email="felipe@email"),
            Usuario(nome="Gabriela", email="gabriela@email"),
            Usuario(nome="Hugo", email="hugo@email"),
            Usuario(nome="Isabela", email="isabela@email"),
            Usuario(nome="João", email="joao@email"),
        ]
        session.add_all(usuarios)
        session.commit()

        # ===========================
        #   RECEITAS (10 instâncias)
        # ===========================
        receitas = [
            Receita(titulo="Bolo de Chocolate", descricao="Bolo simples", usuario_id=1),
            Receita(titulo="Lasanha", descricao="Lasanha clássica", usuario_id=2),
            Receita(titulo="Panqueca", descricao="Panqueca doce", usuario_id=3),
            Receita(titulo="Sopa de Legumes", descricao="Bem nutritiva", usuario_id=4),
            Receita(titulo="Arroz Doce", descricao="Tradicional", usuario_id=5),
            Receita(titulo="Salada Caesar", descricao="Bem leve", usuario_id=6),
            Receita(titulo="Pizza Caseira", descricao="Com borda recheada", usuario_id=7),
            Receita(titulo="Pudim", descricao="Receita clássica", usuario_id=8),
            Receita(titulo="Torta de Frango", descricao="Super cremosa", usuario_id=9),
            Receita(titulo="Frango Assado", descricao="Temperado com ervas", usuario_id=10),
        ]
        session.add_all(receitas)
        session.commit()

        # ===========================
        #   INGREDIENTES (10 instâncias)
        # ===========================
        ingredientes = [
            Ingrediente(nome="Farinha"),
            Ingrediente(nome="Ovo"),
            Ingrediente(nome="Leite"),
            Ingrediente(nome="Chocolate"),
            Ingrediente(nome="Carne"),
            Ingrediente(nome="Queijo"),
            Ingrediente(nome="Tomate"),
            Ingrediente(nome="Açúcar"),
            Ingrediente(nome="Alho"),
            Ingrediente(nome="Sal"),
        ]
        session.add_all(ingredientes)
        session.commit()

        # ===========================
        #   Relação Many-to-Many (30+)
        # ===========================
        relacoes = [
            # Bolo
            ReceitaIngrediente(receita_id=1, ingrediente_id=1),
            ReceitaIngrediente(receita_id=1, ingrediente_id=2),
            ReceitaIngrediente(receita_id=1, ingrediente_id=3),
            ReceitaIngrediente(receita_id=1, ingrediente_id=4),

            # Lasanha
            ReceitaIngrediente(receita_id=2, ingrediente_id=5),
            ReceitaIngrediente(receita_id=2, ingrediente_id=6),
            ReceitaIngrediente(receita_id=2, ingrediente_id=7),

            # Panqueca
            ReceitaIngrediente(receita_id=3, ingrediente_id=1),
            ReceitaIngrediente(receita_id=3, ingrediente_id=2),
            ReceitaIngrediente(receita_id=3, ingrediente_id=3),

            # Sopa de legumes
            ReceitaIngrediente(receita_id=4, ingrediente_id=7),
            ReceitaIngrediente(receita_id=4, ingrediente_id=9),
            ReceitaIngrediente(receita_id=4, ingrediente_id=10),

            # Arroz doce
            ReceitaIngrediente(receita_id=5, ingrediente_id=3),
            ReceitaIngrediente(receita_id=5, ingrediente_id=8),
            ReceitaIngrediente(receita_id=5, ingrediente_id=10),

            # Salada Caesar
            ReceitaIngrediente(receita_id=6, ingrediente_id=6),
            ReceitaIngrediente(receita_id=6, ingrediente_id=7),
            ReceitaIngrediente(receita_id=6, ingrediente_id=10),

            # Pizza caseira
            ReceitaIngrediente(receita_id=7, ingrediente_id=1),
            ReceitaIngrediente(receita_id=7, ingrediente_id=6),
            ReceitaIngrediente(receita_id=7, ingrediente_id=7),

            # Pudim
            ReceitaIngrediente(receita_id=8, ingrediente_id=2),
            ReceitaIngrediente(receita_id=8, ingrediente_id=3),
            ReceitaIngrediente(receita_id=8, ingrediente_id=8),

            # Torta de Frango
            ReceitaIngrediente(receita_id=9, ingrediente_id=5),
            ReceitaIngrediente(receita_id=9, ingrediente_id=6),
            ReceitaIngrediente(receita_id=9, ingrediente_id=1),

            # Frango Assado
            ReceitaIngrediente(receita_id=10, ingrediente_id=5),
            ReceitaIngrediente(receita_id=10, ingrediente_id=9),
            ReceitaIngrediente(receita_id=10, ingrediente_id=10),
        ]

        session.add_all(relacoes)
        session.commit()

    print("🎉 Banco populado com 10 instâncias por entidade!")


if __name__ == "__main__":
    popular_banco()