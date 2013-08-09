#!/usr/bin/python
import plugins
tcp = plugins.tcp(address='ebay.com', port=801, timeout=1)
print tcp.args
(status, data) = tcp.check()
print "status: %s\ndata: %s" % (status, data)


