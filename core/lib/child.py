#HH core child
from time import sleep


def target(child_id):
    print "child created!"
    while True:
        print "I am child %s" % child_id
        sleep(3)


def get_name(child_id):
    return "hh_child_%s" % child_id