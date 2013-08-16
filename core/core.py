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
from multiprocessing import Process, Queue

stdout = sys.stdout  # open('/tmp/stdout', 'a')
stderr = stdout
max_chld = 1
PIDFILE = '/tmp/hh_core.pid'
children = {}


def get_proc_name(pid):
    ps_info = os.popen("ps -p %s -o command hc" % str(pid))
    proc_name = ps_info.read().rstrip()
    return proc_name


def sigterm(signum, frame):
    """ SIGTERM Handler """
    print "[master] Caught sigterm!"
    for (pid, chld) in children.items():
        if chld.is_alive():
            print "[master] Terminating child %s" %pid
            chld.terminate()
            chld.join()
    exit(0)


def sigchld(signum, frame):
    print "SIGCHLD fired"
    # map(lambda child: child.is_alive(), children.values())  # reap zombies


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


def spawn_children():
    # make sure that all children is alive; otherwise remove dead ones from children
    print "spawn called!"
    for (pid, chld) in children.items():
        if not chld.is_alive():
            del children[pid]

    if len(children) >= max_chld:
        print "spawn not needed"
        return

    while len(children) != max_chld:
        print "spawning a child!"
        new_child = Process(
            target=child.target,
            # name=child.get_name(i),
            args=()
        )
        new_child.daemon = True
        new_child.start()
        children[new_child.pid] = new_child
        sleep(2)
        print "[master] fuck yeah"

if __name__ == '__main__':
    context = daemon.DaemonContext(
        working_directory='/',
        umask=0o002,
        pidfile=lock_pidfile(PIDFILE),
        stdout=stdout,
        stderr=stdout,
        signal_map={
            signal.SIGTERM: sigterm,
            signal.SIGCHLD: sigchld
        },
    )

    with context:
        # Write our pid to pidfile
        f = open(context.pidfile.path + '.lock', 'w')
        f.write(str(os.getpid()))
        f.close()

        # Create DB session
        db_session = db.Session()
        print "BEFORE LOOP"
        # Master process' main loop
        while True:
            print "before spawn!"
            spawn_children()
            #for check in db_session.query(db.Checks).order_by(db.Checks.check_id):
            print "master sleep"
            sleep(1000)