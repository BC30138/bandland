"""Настройки роутинга."""

from fastapi import APIRouter, FastAPI

PRIVATE_PATH = "/private"
PUBLIC_PATH = "/public"


def setup_private_router(app: FastAPI) -> None:
    """Настройка приватных путей."""

    router = APIRouter()
    app.include_router(router=router, prefix=PRIVATE_PATH)


def setup_public_router(app: FastAPI) -> APIRouter:
    """Настройка публичных путей."""

    router = APIRouter()
    app.include_router(
        router=router,
        prefix=PUBLIC_PATH,
    )
    return router
