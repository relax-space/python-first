import re
"""
今日回顾：
1.拆分需求：
    统计数量
    统计单词
2.方法：google搜索 关键词（这部分你很有优势）
3.gitlab提交代码
    git add .
    git commit -m "xxx"
    git push origin master

    git clone xxxxxx

python.exe .\ms\1.read.py

"""

content = None
with open("ms/1.txt","r",encoding="utf-8") as fp:
    content = fp.read()

if content != None:
    print(len(content))

word = re.split(r"\W+",content)
word = [v for v in word if len(v.strip()) !=0] # filter word not include empty
print(word)
print(len(word))