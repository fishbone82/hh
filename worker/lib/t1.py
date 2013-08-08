#!/usr/bin/python
import plugins
tcp = plugins.tcp(address='fishbone.me', port=80)
print tcp.args
(status, data) = tcp.check()
print "status: %s\ndata: %s" % (status, data)


