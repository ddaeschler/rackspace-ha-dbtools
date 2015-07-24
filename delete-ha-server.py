#!/usr/bin/env python
#usage: delete-ha-server UUID

import sys
import pyrax
import getopt

from common import init_pyrax

def main(argv):
    if len(argv) != 1:
        print "usage: delete-ha-server UUID";
        return

    init_pyrax()

    for ha in pyrax.cloud_databases.list_ha():
        if ha.id == argv[0]:
            ha.delete()
            break

if __name__ == "__main__":
    main(sys.argv[1:])
