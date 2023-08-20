"""Конфигурация приложения."""

import dataclasses
from urllib.parse import urlparse

from dotenv import dotenv_values


@dataclasses.dataclass
class AppConfiguration:
    database_url: str


def load_app_configuration() -> AppConfiguration:
    """Загружает конфигурацию приложения."""

    dotenv_config = dotenv_values()

    database_url = urlparse(dotenv_config["DATABASE_URL"])

    return AppConfiguration(
        database_url=str(database_url.geturl()),
    )


app_configuration = load_app_configuration()
