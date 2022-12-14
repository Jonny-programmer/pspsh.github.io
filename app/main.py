from fastapi import Depends, FastAPI

from app.config import *
from app.db import database
from .dependencies import get_token_header, oauth2_scheme
from .internal import admin
from .routers import items, users

# Можно вместо этого absolute import: from app.routers import items, users
app = FastAPI(dependencies=[Depends(oauth2_scheme)])

database.global_init(SQLALCHEMY_DATABASE_URI)

app.include_router(users.router)
app.include_router(items.router)
# You can add the same router multiple times with different prefixes This might be useful, for example, when you want
# to expose API under different prefixes, e.g.: /api/v1 and /api/latest
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {'message': 'Hello from the fastapi application!!'}
