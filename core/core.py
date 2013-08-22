#!/usr/bin/python -u
# HH Core daemon
from time import sleep
import daemon
import lockfile
import signal
import os
from child import child_handler
from db import get_rotten_checks
from multiprocessing import Process, active_children, Event, Queue


#STDOUT = sys.stdout
STDOUT = open('/tmp/stdout', mode='w', buffering=0)
STDERR = STDOUT
MAX_CHLD = 1
PIDFILE = '/tmp/hh_core.pid'
MASTER_SLEEP_INTERVAL = 3
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
    STDOUT.flush()
    STDOUT.close()
    STDERR.close()
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
                target=child_handler,
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
        stdout=STDOUT,
        stderr=STDERR,
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

        print "Master started with PID %s" % os.getpid()
        while 1:
            spawn_children(task_queue)
            for check in get_rotten_checks():
                task_queue.put(check)
            sleep(MASTER_SLEEP_INTERVAL)