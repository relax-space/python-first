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


