#!/usr/bin/env python
#usage: list-ha-servers

import sys
import pyrax
import getopt

from common import init_pyrax

def main(argv):
    init_pyrax()

    for ha in pyrax.cloud_databases.list_ha():
        print ha

if __name__ == "__main__":
    main(sys.argv[1:])
