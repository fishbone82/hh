#HH core child
from time import sleep
import signal
import os
import sys
import requests
WORKER_TIMEOUT = 3


def sigterm(signum, frame):
    """ SIGTERM Handler """
    print "[child] %s caught sigterm!" % os.getpid()
    os.abort()


def target(task_queue):
    print "[child] %s created!" % os.getpid()
    signal.signal(signal.SIGTERM, sigterm)

    while True:
        check = task_queue.get()
        check_results = []
        for worker in check.get_workers():
            url = 'http://%s/check/%s' % (worker.address, check.plugin)
            try:
                r = requests.get(url, params=check.args_dict(), timeout=WORKER_TIMEOUT)
                (retcode, data) = r.json()
                check_results.append({
                    'worker_id': worker.worker_id,
                    'retcode': retcode,
                    'data': data,
                })
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                check_results.append({
                    'worker_id': worker.worker_id,
                    'retcode': -1,
                    'data': None,
                })

        # We need to check results here
        # session = get_session()
        # check.next_check = text('now() + check_interval')
        # print 'before %s' % check.next_check
        # session.merge(check)
        # session.flush()
        # print 'after %s' % check.next_check
        check.update_results(check_results)







        #print "Child %s get task %s for workers: %s" % (os.getpid(), check.check_id, check.get_workers())
