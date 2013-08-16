#HH core child
from time import sleep
import signal
import os
import sys


def sigterm(signum, frame):
    """ SIGTERM Handler """
    print "[child] %s caught sigterm!" % os.getpid()
    sys.exit(5)


def target():
    print "[child] %s created!" % os.getpid()

    signal.signal(signal.SIGTERM, sigterm)

    while True:
        # print "[child] %s Zzz.." % os.getpid()
        sleep(3)
