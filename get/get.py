#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi

# http://localhost/cgi/python-first/get/get.py?a=1&b=2
# param a:1,b:2

form = cgi.FieldStorage()

a = form.getvalue('a')
b = form.getvalue('b')

print("Content-type:text/html\r\n\r\n")
print("param a:%s,b:%s" % (a,b))
