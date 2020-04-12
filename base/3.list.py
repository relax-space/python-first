# 集合，字典

# list  CRUD
list2 = [1,2]
print(list2)

print("list ===========")

list = ["go","python"]
print(list)

list.append("java")

print(list)

list.remove("go")

print(list)

list[0]="c#"

print(list)


# map  CRUD

print("map ===========")

map ={"go":1,"python":2}
print(map)

map["java"] = 3
print(map)

del map["go"]
print(map)

map["python"] =100
print(map)


# map2  CRUD : https://www.linuxzen.com/python-you-ya-de-cao-zuo-zi-dian.html

print("map2 ===========")


map2 = dict(name="old",age=1)

print(map2.get("name"))

map2.update({"name":"new"})
print(map2.get("name"))

map2.pop("name")
print(map2)
