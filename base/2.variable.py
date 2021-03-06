# 变量和数据类型

'''
变量：
1.标识符有字母、数字、下划线组成
2.所有标识符可以包括英文、数字以及下划线（_），但不能以数字开头
3.以下划线开头的标识符为私有变量
https://www.w3cschool.cn/python/python-basic-syntax.html
https://blog.csdn.net/qq_31821675/article/details/78022862
'''

'''
在python里，标识符有字母、数字、下划线组成。

在python中，所有标识符可以包括英文、数字以及下划线（_），但不能以数字开头。

python中的标识符是区分大小写的。

以下划线开头的标识符是有特殊意义的。以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入；

以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数。

Python 可以同一行显示多条语句，方法是用分号 ; 分开，
'''

item_one = 1
item_two = 2
item_three = 3
total = item_one + \
    item_two + \
    item_three
print(total)

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)

# 不换行输出
x=1
y="a"
print(x,y)


'''
数据类型：
Numbers（数字）：int，long，float，complex
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）

'''

i = 1
print(type(i))

str = 'hello'
print(str)
print(str[0:1])

