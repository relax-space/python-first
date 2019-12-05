# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     target = 'http://www.biqukan.com/1_1094/5403177.html'
     req = requests.get(url=target)
     print(req.encoding)  # 查看网页返回的字符集类型
     print(req.apparent_encoding)  # 自动判断字符集类型
     req.encoding = req.apparent_encoding
     html = req.text
     bf = BeautifulSoup(html)
     texts = bf.find_all('div', class_='showtxt') 
     print(texts[0].text.replace('\xa0'*8, '\n\n'))
