#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\python.exe

# 导入模块
import os
from http import cookies

print ("Content-type: text/html")
print ()

print ("""
<html>
<head>
<meta charset="utf-8">
<title>W3Cschool教程(w3cschool.cn)</title>
</head>
<body>
<h1>读取cookie信息</h1>
""")

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c=cookies.SimpleCookie()
    c.load(cookie_string)

    try:
        data=c['_mkto_trk'].value
        print ("cookie data: "+data+"<br>")
    except KeyError:
        print ("cookie 没有设置或者已过去<br>")
print ("""
</body>
</html>
""")
