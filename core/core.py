# HH Core
from multiprocessing import Process
import sys
sys.path.append('lib')
import child
import db
from time import sleep
import daemon
import lockfile
import signal

# stdout = open('/tmp/stdout', 'a')
stdout = sys.stdout
stderr = stdout
max_chld = 2
children = []


def sigterm(signum, frame):
    print "TERMINATED by %s at frame %s" % (signum, frame)


context = daemon.DaemonContext(
    working_directory='/',
    umask=0o002,
    pidfile=lockfile.FileLock('/tmp/spam.pid'),
    stdout=stdout,
    stderr=stdout
)

context.signal_map = {
    signal.SIGTERM: sigterm,
    #signal.SIGHUP: sig,
    #signal.SIGUSR1: reload_program_config,
}

with context:
    # Make children
    # for i in xrange(max_chld):
    #     new_child = Process(target=child.target, name=child.get_name(i), args=(i,))
    #     new_child.start()
    #     children.append(new_child)
    #     #new_child.join()

    # Master process' main loop
    while 1:
        print "ZZzz.."
        sleep(1)




# max_chld = 2
#


# db sample
# c = db.Checks(host_id=1, state='-1', plugin='tcp')
# print c.check_interval
# session = db.Session()
# session.add(c)
# session.flush()





