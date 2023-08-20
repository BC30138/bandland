"""Настройки логирования приложения."""

import logging

import yaml


def setup_logger() -> None:
    """Настраивает логирование."""

    with open("log-config.yaml") as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)  # type: ignore
