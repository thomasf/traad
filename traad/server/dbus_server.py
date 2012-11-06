import os

import baker
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from traad.rope_interface import RopeInterface
from traad.server.log import init_logging, log, log_basic_info

class DBusServer(dbus.service.Object):
    def __init__(self, rope_if, object_path):
        dbus.service.Object.__init__(self, dbus.SessionBus(), object_path)
        self.rope_if = rope_if

    @dbus.service.method(dbus_interface='traad.ProjectServer',
                         in_signature='', out_signature='a(sb)')
    def get_all_resources(self):
        return self.rope_if.get_all_resources()

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

    server = DBusServer(
        RopeInterface(project),
        '/traad/ProjectServer')

    main_loop = DBusGMainLoop(set_as_default=True)
