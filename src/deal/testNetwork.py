import requests
import json


# from requests.api import request
# from requests.models import Response
url = "http://127.0.0.1:5000/circular_OGDF_layout"  # 接口地址

# 消息头数据
# headers = {
#             'Connection': 'keep-alive',
#             'Content-Length': '123',
#             'Cache-Control': 'max-age=0',
#             'Origin':'https://passport.csdn.net',
#             'Upgrade-Insecure-Requests':'1',
#             'Content-Type': 'application/x-www-form-urlencoded',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#             'Referer': 'https://passport.csdn.net/account/login?from=http://www.csdn.net',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Accept-Language': 'zh-CN,zh;q=0.9',
#             'Cookie': '省略', 
#             }
headers = {'Content-Type': 'application/json','Connection': 'keep-alive'}
payload = {
            "nodes": [
                {
                    "id": "1583"
                },
                {
                    "id": "1599"
                },
                {
                    "id": "1529"
                },
                {
                    "id": "1510"
                },
                {
                    "id": "1544"
                },
                {
                    "id": "1573"
                },
                {
                    "id": "1549"
                },
                {
                    "id": "1525"
                },
                {
                    "id": "1523"
                },
                {
                    "id": "1602"
                },
                {
                    "id": "1631"
                }
            ],
            "links": [
                {
                    "source": "1583",
                    "target": "1599"
                },
                {
                    "source": "1583",
                    "target": "1510"
                },
                {
                    "source": "1599",
                    "target": "1529"
                },
                {
                    "source": "1599",
                    "target": "1510"
                },
                {
                    "source": "1599",
                    "target": "1523"
                },
                {
                    "source": "1544",
                    "target": "1573"
                },
                {
                    "source": "1549",
                    "target": "1525"
                },
                {
                    "source": "1602",
                    "target": "1631"
                }
            ]
        }
# verify = False 忽略SSH 验证 
data=json.dumps({"graph":payload})
# time.sleep(0.5)
r = requests.post(url, data=data,headers=headers)
r.close()
# Response.close()
print (r.text)
