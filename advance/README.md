

https://www.w3cschool.cn/python/python-cgi.html


1. install apache in windows
   http://httpd.apache.org/

2. httpd.conf

```
<Directory "${SRVROOT}/cgi-bin">
   AllowOverride None
   Options +ExecCGI
   Require all granted
</Directory>

AddHandler cgi-script .cgi .pl .py

```

3. put py file into cgi-bin

access path: http://localhost/cgi-bin/hello.py

```
#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\python.exe

print("Content-type:text/html\r\n\r\n")
print('hello cgi')

```

4. custom path

access path: http://localhost/cgi/python-first/advance/cgi.py

```
Define SRVPATH "D:\source\pythonpath"

ScriptAlias /cgi/ "${SRVPATH}/"

<Directory "${SRVPATH}">
   AllowOverride None
   Options +ExecCGI
   Require all granted
</Directory>
```



