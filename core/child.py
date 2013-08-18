#HH core child
from time import sleep
import signal
import os
import sys
import requests


def sigterm(signum, frame):
    """ SIGTERM Handler """
    print "[child] %s caught sigterm!" % os.getpid()
    os.abort()


def target(task_queue):
    print "[child] %s created!" % os.getpid()
    signal.signal(signal.SIGTERM, sigterm)

    while True:
        check = task_queue.get()
        for worker in check.get_workers():
            url = 'http://%s/check/%s' % (worker.address, check.plugin)
            r = requests.get(url, params=check.args_dict())
            print r.json()



        #print "Child %s get task %s for workers: %s" % (os.getpid(), check.check_id, check.get_workers())
