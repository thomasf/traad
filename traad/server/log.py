import logging
import sys

log = logging.getLogger('traad.server')

def init_logging(verbosity):
    level = {
        0: logging.WARNING,
        1: logging.INFO,
        2: logging.DEBUG
    }[verbosity]

    logging.basicConfig(
        level=level)

def log_basic_info():
    log.info('Python version: {}'.format(sys.version))
