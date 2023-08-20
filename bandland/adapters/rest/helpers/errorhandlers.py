"""Обработчики rest-ошибок."""

import http

from fastapi import Request
from fastapi.responses import JSONResponse

from bandland.adapters.rest.helpers.responses import ResponseStatus

INTERNAL_ERROR_CODE = "INTERNAL_ERROR"


async def internal_error_exception_handler(
    _request: Request,  # noqa: U101
    exc: Exception,
) -> JSONResponse:
    return JSONResponse(
        content={
            "status": ResponseStatus.error.value,
            "code": getattr(exc, "code", INTERNAL_ERROR_CODE),
            "error_msg": str(exc),
        },
        status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,
    )
