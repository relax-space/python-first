# 对象

class Student:
    name =''

    def __init__(self,name='iu'):
        self.name = name
    
    def sayHi(self):
        print("hello,my name is %s" % self.name)


s = Student('xiaoxinmiao')
s.sayHi()
