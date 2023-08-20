"""Точка запуска приложения."""

import uvicorn
from fastapi import FastAPI

from bandland.adapters.rest.helpers.errorhandlers import internal_error_exception_handler

# Инициация конфигурации
from bandland.cfg import app_configuration  # noqa
from bandland.log import setup_logger
from bandland.routes import PRIVATE_PATH, setup_private_router, setup_public_router


def setup_app() -> FastAPI:
    """Фабрика для создания приложения."""

    app_instance = FastAPI(
        docs_url=f"{PRIVATE_PATH}/swagger",
        exception_handlers={Exception: internal_error_exception_handler},  # noqa: B902
    )

    setup_logger()

    setup_private_router(app=app_instance)
    setup_public_router(app=app_instance)

    return app_instance


app = setup_app()


if __name__ == "__main__":
    uvicorn.run("bandland.app:app", host="127.0.0.1", port=8000, reload=True)
