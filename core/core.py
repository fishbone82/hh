#!/usr/bin/python
# HH Core daemon
from time import sleep
import daemon
import lockfile
import signal
import os
from multiprocessing import Process

import sys
sys.path.append('lib')
import child
import db


stdout = sys.stdout  # open('/tmp/stdout', 'a')
stderr = stdout
max_chld = 1
PIDFILE = '/tmp/hh_core.pid'
children = []


def get_proc_name(pid):
    ps_info = os.popen("ps -p %s -o command hc" % str(pid))
    proc_name = ps_info.read().rstrip()
    return proc_name


def sigterm(signum, frame):
    """ SIGTERM Handler """
    print "master caught sigterm"
    for chld in children:
        print "terminating child.."
        chld.terminate()
        chld.join()
    exit()


def lock_pidfile(filename):
    pidfile = lockfile.FileLock(filename)
    try:
        pidfile.acquire(1)
    except lockfile.LockTimeout:
        # Lock timeout. We must read pid from file and decide is it valid or not
        try:
            f = open(filename + '.lock', 'r')
            pid = f.read()

            if not pid or not int(pid) > 0:
                raise Exception("invalid pid in pidfile")

            #check if proc_name of pid in pidfile equals to self proc_name
            if get_proc_name(pid) == get_proc_name(os.getpid()):
                print "Can't start core - another process with PID %s already running" % pid
                exit(1)
            raise Exception("rotten pidfile")
        except Exception:
            # Couldn't read file - delete it and try to lock again!
            os.remove(filename + '.lock')
            return lock_pidfile(filename)
    return pidfile


if __name__ == '__main__':
    context = daemon.DaemonContext(
        working_directory='/',
        umask=0o002,
        pidfile=lock_pidfile(PIDFILE),
        stdout=stdout,
        stderr=stdout,
        signal_map={
            signal.SIGTERM: sigterm,
        }
    )

    with context:
        f = open(context.pidfile.path + '.lock', 'w')
        f.write(str(os.getpid()))
        f.close()
        # Make children
        for i in xrange(max_chld):
            new_child = Process(target=child.target, name=child.get_name(i), args=(i,))
            new_child.start()
            children.append(new_child)

        # Master process' main loop
        while 1:
            print "ZZzz.."
            sleep(5)

# db sample
# c = db.Checks(host_id=1, state='-1', plugin='tcp')
# print c.check_interval
# session = db.Session()
# session.add(c)
# session.flush()





