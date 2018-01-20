import urllib.request
import re,os
import time
import matplotlib.pyplot as plt


name = 'gl486546'

CSDN_blog_url = 'http://blog.csdn.net/' + name

def get_maxlistNum():
	rps = urllib.request.urlopen(CSDN_blog_url)
	html = rps.read().decode('utf-8')
	x = re.findall(r'/article/list/([0-9]+)">尾页</a>',html)
	if x:
		return int(x[0])
	print('not found\n')
	return 1

def fetch_data():
	num = get_maxlistNum()
	prefix_url = 'http://blog.csdn.net/'+ name +'/article/list/' 
	mylist = []
	for i in range(1,num+1):
		url = prefix_url + str(i)
		rps = urllib.request.urlopen(url)
		html = rps.read().decode('utf-8')
		x = re.findall(r'<span class="link_title"><a href="/.+/article/details/(.+)">\s*([\s\S]*?)\s*</a>[\s\S]+?title="阅读次数">阅读</a>\((.+)\)',html)
		for e in x:
			li = list(e);
			li[1] = re.sub(r'<.+?>(.+)</.+?>\s+',' ',li[1])
			mylist.append(li)
	file_name = time.strftime('%Y-%m-%d-%H',time.localtime(time.time())) + '.txt'
	mylist.sort(key=lambda x:x[0])
	print(len(mylist))
	with open(file_name,'w',encoding='utf-8') as f:
		for e in mylist:
			f.write(str(e)+'\n')
	os.startfile(file_name)



fetch_data()
