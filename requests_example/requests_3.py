# -*- coding:utf-8 -*-  
import requests
keyword = "Python"
try:
	kv = {'wd':keyword}  #��ȡ360�Ļ� kv = {'q':keyword} 
	r = requests.get("http://www.baidu.com/s",params=kv)
	print(r.request.url)
	r.raise_for_status()
	print(len(r.text)
except:
	print("��ȡʧ��")