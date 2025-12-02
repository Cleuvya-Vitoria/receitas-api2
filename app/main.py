# app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .routers import usuarios, receitas, ingredientes, receita_ingrediente

app = FastAPI(title="API de Receitas Culinárias", version="1.0.0")


# ================================
# HANDLER GLOBAL PARA EXCEÇÕES
# ================================
@app.exception_handler(Exception)
async def excecao_generica_handler(request: Request, exc: Exception):
    """
    Captura exceptions inesperadas e evita travar o servidor.
    """
    return JSONResponse(
        status_code=500,
        content={
            "erro": "Erro interno no servidor.",
            "detalhes": str(exc),
        }
    )


# ================================
# REGISTRO DOS ROUTERS
# ================================
app.include_router(usuarios.router)
app.include_router(receitas.router)
app.include_router(ingredientes.router)
app.include_router(receita_ingrediente.router)