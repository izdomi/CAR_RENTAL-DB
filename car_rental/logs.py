import logging


def get_logger(name, level=logging.INFO, fmt=None):
    logger = logging.getLogger(name=name)
    logger.setLevel(level)

    handler = logging.StreamHandler()

    if fmt is None:
        fmt = "%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s"
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
