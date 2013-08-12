#HH core child
from time import sleep
import signal


def sigterm(signum, frame):
    """ SIGTERM Handler """
    print "child caught sigterm"
    exit(0)


def target(child_id):
    print "child created!"

    # signal handlers
    signal.signal(signal.SIGTERM, sigterm)

    while True:
        print "I am child %s" % child_id
        sleep(3)


def get_name(child_id):
    return "hh_child_%s" % child_id