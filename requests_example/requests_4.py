# -*- coding:utf-8 -*-  
#��ȡͼƬ
import requests
import os
url = "http://image.nationalgeographic.com.cn/2017/0315/20170315045734460.jpg"
root = "D://pic//"    #·��
path = root +url.split('/')[-1]
try:
	if not os.path.exists(root)
		os.mkdir(root)
	if not os.path.exists(path)
		r = requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("�ļ�����ɹ�")
	else:
		print("�ļ��Ѿ�����")
except:
	print("��ȡʧ��")