#!/usr/bin/env python
#usage: ha-server-details UUID

import sys
import pyrax
import getopt
import pprint

from common import init_pyrax

def main(argv):
    if len(argv) != 1:
        print "usage: ha-server-details UUID";
        return

    init_pyrax()

    for ha in pyrax.cloud_databases.list_ha():
        if ha.id == argv[0]:
            ha.get()
            print ha
            break

if __name__ == "__main__":
    main(sys.argv[1:])
