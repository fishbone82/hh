#!/usr/bin/python
import plugins
tcp = plugins.tcp(
    address='ebay.com',
    port=80,
    # timeout=1,
    # critical_time=0.3,
    # warning_time=0.22,
)
print 'Plugin args:', tcp.args
(status, data) = tcp.check()
print "status: %s\ndata: %s" % (status, data)


