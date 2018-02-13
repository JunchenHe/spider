#!/usr/bin/env python3
import requests
user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
headers={'User_Agent':user_agent}
cookies=dict(name='qiye',age='10')
#r=requests.get('http://www.baidu.com',headers=headers)
r=requests.get('http://www.baidu.com',headers=headers,cookies=cookies)
r.encoding=r.apparent_encoding
print(r.text)
