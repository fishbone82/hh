#HH core child
from time import sleep
import signal


def sigterm(signum, frame):
    """ SIGTERM Handler """
    print "child caught sigterm"
    exit(0)


def target(child_id, task_queue):
    print "child created!"

    # signal handlers
    signal.signal(signal.SIGTERM, sigterm)

    while True:
        #print "I am child %s" % child_id
        task = task_queue.get()
        if task is not None:
            print "Child %s get task: %s" % (child_id, task)
        sleep(1)

def get_name(child_id):
    return "hh_child_%s" % child_id