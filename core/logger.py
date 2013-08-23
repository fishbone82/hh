from time import strftime


def log(message='Empty message', originator='UNKNOWN'):
    print "%s [%s %s] %s" % (strftime('%Y-%m-%d %H:%M:%S'), originator, os.getpid(), message)