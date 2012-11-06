import os
import sys

import baker
from traad.rope_interface import RopeInterface
from traad.server.log import init_logging, log, log_basic_info


major_version = sys.version_info.major

if major_version == 2:
    from SimpleXMLRPCServer import SimpleXMLRPCServer
    from xmlrpclib import ServerProxy

elif major_version == 3:
    from xmlrpc.client import ServerProxy
    from xmlrpc.server import SimpleXMLRPCServer

else:
    assert False, 'Only supported on Python 2 and 3. Your version = {}'.format(
        sys.version)

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
    """Run an XMLRPC-based traad server.
    """
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
