#!/usr/bin/env python
#usage: delete-ha-server-acl UUID address

import sys
import pyrax
import getopt
import pprint

from common import init_pyrax

def main(argv):
    if len(argv) != 2:
        print "usage: delete-ha-server-acl UUID address";
        return

    init_pyrax()

    for ha in pyrax.cloud_databases.list_ha():
        if ha.id == argv[0]:
            for acl in ha.list_acls():
                if acl.address == argv[1]:
                    acl.delete()

if __name__ == "__main__":
    main(sys.argv[1:])
