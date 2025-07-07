import logging


def init_logger():
    level = logging.DEBUG
    format = "{asctime} - {levelname} - {name} - {message}"

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
    formatter = logging.Formatter(
        format,
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logging.basicConfig(
        level=level,
        format=format,
        style="{",
        datefmt="%Y-%m-%d %H:%M",
        handlers=[file_handler, console_handler],
    )
