#!/usr/bin/env python3
import requests
user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
headers={'User_Agent':user_agent}
r=requests.get("http://www.baidu.com",headers=headers)
for cookie in r.cookies.keys():
    print(cookie+':'+r.cookies.get(cookie))
