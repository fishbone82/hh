# Orthus tcp plugin
import socket
from time import time
from base import plugin_base
from args import address, port, timeout, critical_time, warning_time


class plugin(plugin_base):
    use_args = (address, port, timeout, critical_time, warning_time)
    description = "Simple TCP plugin for Orthus"

    def process(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self.args['timeout'])
        start_time = time()
        try:
            s.connect((self.args['address'], self.args['port']))
        except socket.timeout:
            self.status = 2
            self.data = 'Connection timed out'
            return
        except socket.error:
            self.status = 2
            self.data = "Socket error(can't resolve?)"
            return
        time_spent = float('%.3f' % (time() - start_time))
        self.data = {"time_spent": time_spent}

        # result processing
        if time_spent > self.args['critical_time']:
            self.status = 2
        elif time_spent > self.args['warning_time']:
            self.status = 1
        else:
            self.status = 0