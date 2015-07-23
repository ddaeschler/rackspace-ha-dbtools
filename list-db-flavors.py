#!/usr/bin/env python
#usage: list-db-flavors

import sys
import pyrax
import getopt

def main(argv):
    pyrax.set_setting("identity_type", "rackspace")
    pyrax.set_credential_file('credentials.conf')

    for flav in pyrax.cloud_databases.list_flavors():
        print flav

if __name__ == "__main__":
    main(sys.argv[1:])
