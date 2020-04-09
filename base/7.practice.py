
# import os

# print(type(os.environ.keys()))


# for key in os.environ.keys():
#     print(key, os.environ[key])

import time,random


dict1 ={':authority': 'login.taobao.com', ':method': 'POST', ':path': '/member/login.jhtml', ':scheme': 'https', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7', 'cache-control': 'max-age=0', 'content-length': '2630', 'content-type': 'application/x-www-form-urlencoded', 'cookie': '_uab_collina=158266152636970738514848; thw=cn; _fbp=fb.1.1582661525396.834079526; hng=AU%7Czh-CN%7CAUD%7C36; enc=PsiZve3L1C6VWBQqAjt7YP2LTYbT5GlhZokxVsQly0AK%2ByQLt4p53PH4tgRudwssmOfMd8L9ErfmpZj4WuG2dA%3D%3D; t=a6c4b5a5ef162bebde6fb8025c5dd9ee; cna=j23cFk7OygcCAd9IVESfg2pS; sgcookie=DLtBuR%2BGVrjdqrpHiecYH; uc3=id2=VAYhfVsUHpas&lg2=V32FPkk%2Fw0dUvg%3D%3D&nk2=G4mgLCtQ61Ct4Q%3D%3D&vt3=F8dBxd34DJjkYJWIe3g%3D; log=lty=Ug%3D%3D; lgc=xiaoxm_001; uc4=id4=0%40Vh%2BzeYCIjUuF6BHgS5Vb5rG5Qwc%3D&nk4=0%40GToWF7xjYYbAUv7x%2FoIxGIUNGMc3; tracknick=xiaoxm_001; lc=Vyu3oQ4feSXepMZl6ScL; _cc_=W5iHLLyFfA%3D%3D; lid=xiaoxm_001; tg=0; mt=ci=-1_1; _samesite_flag_=true; cookie2=12be6357d02dc8630499dd6a83d01511; _tb_token_=e185bdb6beb46; isg=BMjIpyvYAopYGW46TftocnKzmTbacSx7xCLXkoJ5FMM2XWjHKoH8C15f0T0t9uRT; tfstk=cF8FBbVRt23ElqiicZ7PFiABMzAdwsAHZP5fxnqXrNOpA6fDc8C6S-CNNt3Gx; l=dBrBq5egQiboDfSbBOCanurza77OSIRYYuPzaNbMi_5dQ6T6to7Ooo1uhF96VfWf9BLB4aVvW6J9-etkZQDmndIpXUJ6CxDc.', 'origin': 'https://login.taobao.com', 'referer': 'https://login.taobao.com/member/login.jhtml', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

foodict = {k: v for k, v in dict1.items() if k.startswith(':')==False}
print(foodict)
# newDict ={}
# for k,v in dict1.items():
#     if k.startswith(":") == False:
#         newDict[k]=v

# print(dict1)



# for i in range(1,30):
#     time.sleep(random.randint(1000,3000)/1000)
#     print(random.randint(1000,3000)/1000)


class NameValueDto:
    def __init__(self):
        self.name =""
        self.value=""

names={"name1":"111","name2":"222"}
for name,value in names.items():
    if name =="name1":
        names[name]="change"
print(names)



li = [{"name1":"111","name2":"222"},{"name1":"1111","name2":"2222"}]

for l in li:
    if l.get("name1") == "111":
        l["name1"]="change"

print(li)