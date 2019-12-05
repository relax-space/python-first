爬虫流程：

- 先由urllib的request打开Url得到网页html文档

- 浏览器打开网页源代码分析元素节点

- 通过Beautiful Soup或则正则表达式提取想要的数据

- 存储数据到本地磁盘或数据库（抓取，分析，存储）