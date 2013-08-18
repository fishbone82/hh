#HH core child
from time import sleep
import signal
import os
import sys
import Queue


def sigterm(signum, frame):
    """ SIGTERM Handler """
    print "[child] %s caught sigterm!" % os.getpid()
    os.abort()


def target(task_queue):
    print "[child] %s created!" % os.getpid()
    signal.signal(signal.SIGTERM, sigterm)

    while True:
        try:
            task = task_queue.get(timeout=1)
            print "Child %s get task %s" % (os.getpid(), task['id'])
        except Queue.Empty:
            pass
