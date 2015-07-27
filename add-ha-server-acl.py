#!/usr/bin/env python
#usage: add-ha-server-acl UUID address

import sys
import pyrax
import getopt
import pprint

from common import init_pyrax

def main(argv):
    if len(argv) != 2:
        print "usage: add-ha-server-acl UUID address";
        return

    init_pyrax()

    for ha in pyrax.cloud_databases.list_ha():
        if ha.id == argv[0]:
            ha.add_acl(argv[1])
            break

if __name__ == "__main__":
    main(sys.argv[1:])
