#HH core child
from time import sleep
import signal
import os
import sys
import requests
WORKER_TIMEOUT = 3
from db import Mongo
mongo = Mongo.mydb

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
                result = {'worker_id': worker.worker_id, 'data': None}
                if e.__class__ is requests.exceptions.ConnectionError:
                    result['retcode'] = 3
                else:
                    result['retcode'] = 4
                check_results.append(result)
        check.update_next_check_time(check_results)
        collection = mongo.TestData
        collection.insert({"check_id": check.check_id, "results": check_results})
