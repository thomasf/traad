import os

import baker
from traad.rope_interface import RopeInterface
from traad.server.log import init_logging, log, log_basic_info


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
