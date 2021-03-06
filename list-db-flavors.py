#!/usr/bin/env python
#usage: list-db-flavors

import sys
import pyrax
import getopt

from common import init_pyrax

def main(argv):
    init_pyrax()

    for flav in pyrax.cloud_databases.list_flavors():
        print flav

if __name__ == "__main__":
    main(sys.argv[1:])
