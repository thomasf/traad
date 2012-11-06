import os

import baker


# Import the server types so that they can register their baker
# commands.
# TODO: This could/should be done via plugins.
import traad.server.dbus_server
import traad.server.xmlrpc

def main():
    baker.run()

if __name__ == '__main__':
    main()
