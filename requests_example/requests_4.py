# -*- coding:utf-8 -*-  
#爬取图片
import requests
import os
url = "http://image.nationalgeographic.com.cn/2017/0315/20170315045734460.jpg"
root = "D://pic//"    #路径
path = root +url.split('/')[-1]
try:
	if not os.path.exists(root)
		os.mkdir(root)
	if not os.path.exists(path)
		r = requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("文件保存成功")
	else:
		print("文件已经存在")
except:
	print("爬取失败")