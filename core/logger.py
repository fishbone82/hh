from time import strftime
from os import getpid


def log(message='Empty message', originator='UNKNOWN'):
    print "%s [%s %s] %s" % (strftime('%Y-%m-%d %H:%M:%S'), originator, getpid(), message)