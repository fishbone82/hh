# HH Core daemon
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
    """ SIGTERM Handler """
    print "master caught sigterm"
    for chld in children:
        print "terminating child.."
        chld.terminate()
        chld.join()
    exit()


context = daemon.DaemonContext(
    working_directory='/',
    umask=0o002,
    pidfile=lockfile.FileLock('/tmp/spam.pid'),
    stdout=stdout,
    stderr=stdout,
    signal_map={
        signal.SIGTERM: sigterm,
    }
)


with context:
    # Make children
    for i in xrange(max_chld):
        new_child = Process(target=child.target, name=child.get_name(i), args=(i,))
        new_child.start()
        children.append(new_child)

    # Master process' main loop
    while 1:
        print "ZZzz.."
        sleep(1)

# db sample
# c = db.Checks(host_id=1, state='-1', plugin='tcp')
# print c.check_interval
# session = db.Session()
# session.add(c)
# session.flush()





