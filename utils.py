import logging
import logging.handlers


def logger_setup(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler(
        'veileder.log',
        maxBytes=1 * 1024 * 1024,
        backupCount=1)
    formatter = logging.Formatter("%(asctime)s - %(name)s [%(levelname)s] \
    %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
