"""Утилиты для построения ответа."""

import enum


class ResponseStatus(enum.Enum):
    success = "success"
    error = "error"
