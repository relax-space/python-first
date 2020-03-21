import time 
from datetime import datetime, timezone, timedelta 
"""
https://juejin.im/post/5cf522eb6fb9a07ec56e6392
https://www.liaoxuefeng.com/wiki/1016959663602400/1017648783851616

"""


# 无论是在北京电脑，还是utc时间的服务器，都能正确等到timestamp,所以，对于timestamp来说，不需要有任何的时区转换
print(time.mktime(datetime.now().timetuple()))
print(datetime.fromtimestamp(1584830988.0))







