#!/usr/bin/env python
#usage: new-ha-cluster NAME NUM_SLAVES VOLUME FLAVOR_ID
#eg: new-ha-cluster MyCluster 2 1 1

import sys
import pyrax
import getopt

from common import init_pyrax
from pyrax.clouddatabases import CloudDatabaseSpec


def main(argv):
    if (len(argv) < 4):
        print "usage: new-ha-cluster NAME NUM_SLAVES VOLUME FLAVOR_ID"
        return

    init_pyrax()

    #the master
    master = CloudDatabaseSpec(argv[0] + "_master", argv[2], int(argv[3]))

    #build a list of slaves
    slaves = []
    for i in xrange(int(argv[1])):
        slaves.append(CloudDatabaseSpec(argv[0] + "_slave_" + str(i), argv[2], int(argv[3])))

    print pyrax.cloud_databases.create_ha(argv[0], "MYSQL", "5.6", master, slaves)

if __name__ == "__main__":
    main(sys.argv[1:])
