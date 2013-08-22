#HH core child
import signal
import os
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
        workers = check.get_workers()
        for worker in workers:
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
        check.update_results(check_results)
