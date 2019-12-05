#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 2,
    'name': 'W3CSchool',
    'url': 'http://www.w3cschool.cn'
}

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)


print("write success \r\n   you can see in data.json")



with open('datar.json', 'r') as f:
    data2 = json.load(f)

print("read success: \r\n",data2)
