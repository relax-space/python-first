# 流程判断（for if switch）

books = ["go","python"]

for v in books:
    if v == "go":
        print(v)

for v in books:
    if v == "go":
        books.remove(v) 

print(books)

print("map ========")


def removeKey(d, key):
    r = dict(d)
    del r[key]
    return r


mapBooks ={"go":1,"python":2}

for key in mapBooks:
    if key =="go":
        print(key,mapBooks[key])

newBooks=removeKey(mapBooks,"go")

print(newBooks)


d1 = []

for index in range(0,345):
    d1.append(str(index))
print(d1)
n = 100
print([d1[i:i + n] for i in range(0, len(d1), n)])
    

