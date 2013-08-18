#HH core child
from time import sleep
import signal
import os
import sys


def sigterm(signum, frame):
    """ SIGTERM Handler """
    print "[child] %s caught sigterm!" % os.getpid()
    os.abort()


def target(task_queue):
    print "[child] %s created!" % os.getpid()
    signal.signal(signal.SIGTERM, sigterm)

    while True:
        task = task_queue.get()
        check = task['check']
        print "Child %s get task %s with args %s" % (os.getpid(), check.check_id, check.args_decoded())
