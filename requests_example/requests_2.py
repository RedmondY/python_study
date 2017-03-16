# -*- coding:utf-8 -*-  
import requests
url = "https://www.amazon.cn/é£Ÿå“/dp/B00JWJ366U"
try:
	kv = {'user-agent':'Mozilla/5.0'}
	r = requests.get(url,headers=kv)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[1000:2000])
except:
	print("ÅÀÈ¡Ê§°Ü")