#HH core child
import signal
import os
import requests
WORKER_TIMEOUT = 3


def log(message):
    print "[child %s] %s" % (os.getpid(), message)


def sigterm(signum, frame):
    """ SIGTERM Handler """
    log("caught sigterm!")
    os.abort()


def child_handler(task_queue):
    log("process started")
    signal.signal(signal.SIGTERM, sigterm)

    while True:
        check = task_queue.get()
        log("got check %s" % check.check_id)
        check_results = []
        workers = check.get_workers()
        for worker in workers:
            url = 'http://%s/check/%s' % (worker.address, check.plugin)
            try:
                r = requests.get(url, params=check.args_dict(), timeout=WORKER_TIMEOUT)
                (retcode, data) = r.json()
                check_results.append({
                    'worker_id': worker.worker_id,
                    'retcode': retcode,  # 0 - OK, 1 - WARNING, 2 - CRITICAL
                    'data': data,
                })
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                result = {'worker_id': worker.worker_id, 'data': None}
                if e.__class__ is requests.exceptions.ConnectionError:
                    result['retcode'] = 3  # Connection Error
                else:
                    result['retcode'] = 4  # Connection Timeout
                check_results.append(result)
        log("done check %s: %s" % (check.check_id, check_results))
        check.update_results(check_results)
