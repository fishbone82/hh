#Orthus core child
import signal
import os
import requests
import logger
WORKER_TIMEOUT = 3
MAX_TASKS = 1000  # How many tasks can process child in his life


def log(message):
    logger.log(message, 'child')


def sigterm(signum, frame):
    """ SIGTERM Handler """
    log("caught sigterm!")
    os.abort()


def child_handler(task_queue):
    log("process started")
    signal.signal(signal.SIGTERM, sigterm)

    for i in xrange(MAX_TASKS):
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
    log("I've processed %s tasks. My life is over." % MAX_TASKS)
    exit(0)