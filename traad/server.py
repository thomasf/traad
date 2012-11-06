import logging
import os
import sys

import baker

from .rope_interface import RopeInterface

log = logging.getLogger(__name__)

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

@baker.command(
    default=True,
    params={
        'port': 'The port on which the server will listen.',
        'project': 'The directory containing the project to server.',
        'verbosity': 'Verbosity level (0=normal, 1=info, 2=debug).',
    },
    shortopts={
        'port': 'p',
        'verbosity': 'v',
    })
def xmlrpc(project, port=6942, verbosity=0):
    from .xmlrpc import SimpleXMLRPCServer

    init_logging(verbosity)

    log_basic_info()

    log.info(
        'Running traad xmlrpc server for project "{}" on port {}'.format(
            os.path.abspath(project),
            port))

    server = SimpleXMLRPCServer(
        ('127.0.0.1', port),
        logRequests=True,
        allow_none=True)

    server.register_instance(
        RopeInterface(project))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        log.info('Keyboard interrupt')

@baker.command(
    default=True,
    params={
        'project': 'The directory containing the project to server.',
        'verbosity': 'Verbosity level (0=normal, 1=info, 2=debug).',
    },
    shortopts={
        'verbosity': 'v',
    })
def dbus(project, verbosity=0):
    init_logging(verbosity)

    log_basic_info()

    log.info(
        'Running traad dbus server for project "{}".'.format(
            os.path.abspath(project)))

    rope_if = RopeInterface(project)


def main():
    baker.run()

if __name__ == '__main__':
    main()
