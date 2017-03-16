# -*- coding:utf-8 -*-  
import requests
keyword = "Python"
try:
	kv = {'wd':keyword}  #爬取360的话 kv = {'q':keyword} 
	r = requests.get("http://www.baidu.com/s",params=kv)
	print(r.request.url)
	r.raise_for_status()
	print(len(r.text)
except:
	print("爬取失败")