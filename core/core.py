#!/usr/bin/python
# HH Core daemon
from time import sleep
import daemon
import lockfile
import signal
import os
import sys
import child
import db
from db.checks import Check as CheckClass
from multiprocessing import Process, active_children, Event, Queue

stdout = sys.stdout
#stdout = open('/tmp/stdout', mode='w', buffering=0)

stderr = stdout
max_chld = 3
PIDFILE = '/tmp/hh_core.pid'
SPAWN_ALLOWED = True


def get_proc_name(pid):
    ps_info = os.popen("ps -p %s -o command hc" % str(pid))
    proc_name = ps_info.read().rstrip()
    return proc_name


def sigterm(signum, frame):
    """ SIGTERM Handler """
    print "[master] Caught sigterm!"
    global SPAWN_ALLOWED
    SPAWN_ALLOWED = False
    for chld in active_children():
        if chld.is_alive():
            print "[master] Terminating child %s" % chld.pid
            chld.terminate()
            chld.join()
    stdout.close()
    stderr.close()

    exit(0)


def sigchld(signum, frame):
    #print "SIGCHLD fired for %s" % os.getpid()
    ignore = active_children()


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


def spawn_children(queue):
    # spawn children if allowed and needed
    global SPAWN_ALLOWED
    if SPAWN_ALLOWED and len(active_children()) < max_chld:
        while len(active_children()) != max_chld:
            new_child = Process(
                target=child.target,
                kwargs={
                    "task_queue": queue,
                },
            )
            new_child.start()

if __name__ == '__main__':
    context = daemon.DaemonContext(
        working_directory='/',
        umask=0o002,
        pidfile=lock_pidfile(PIDFILE),
        stdout=stdout,
        stderr=stdout,
        signal_map={
            signal.SIGTERM: sigterm,
            signal.SIGCHLD: sigchld,
        },
    )

    with context:
        # Write our pid to pidfile
        f = open(context.pidfile.path + '.lock', 'w')
        f.write(str(os.getpid()))
        f.close()

        # Create queue
        task_queue = Queue()

        print "\nMaster started: %s" % os.getpid()

        while 1:
            spawn_children(task_queue)
            session = db.Session()
            for check in session.query(CheckClass).order_by(CheckClass.check_id):
                task_queue.put(check)
            session.close()
            sleep(3)