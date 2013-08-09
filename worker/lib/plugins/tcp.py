# tcp plugin for HH
from base import plugin_base
from args import address, port, timeout
from time import time
import socket


class plugin(plugin_base):
    use_args = (address, port, timeout)
    description = "Simple TCP plugin for HH"

    def process(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self.args['timeout'])
        start_time = time()
        try:
            s.connect((self.args['address'], self.args['port']))
        except socket.timeout:
            self.status = 2
            self.data = 'Connection timed out'
        time_spent = time() - start_time
        self.status = 0
        self.data = {"time_spent": time_spent}