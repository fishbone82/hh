# HH Core
# from multiprocessing import Process
import sys
sys.path.append('lib')
import child
import db
from time import sleep
import daemon
import lockfile

# stdout = open('/tmp/stdout', 'a')
stdout = sys.stdout
stderr = stdout

context = daemon.DaemonContext(
    working_directory='/',
    umask=0o002,
    pidfile=lockfile.FileLock('/tmp/spam.pid'),
    stdout=stdout
)

with context:
    for i in xrange(10):
        print "it works!"
        sleep(2)

# max_chld = 2
#
# for i in xrange(max_chld):
#     new_child = Process(target=child.target, name=child.get_name(i))
#     new_child.start()
#     # new_child.join()

# db sample
# c = db.Checks(host_id=1, state='-1', plugin='tcp')
# print c.check_interval
# session = db.Session()
# session.add(c)
# session.flush()





