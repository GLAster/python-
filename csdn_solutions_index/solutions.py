import urllib.request
import re,os

prefix_url = "http://blog.csdn.net/gl486546/article/category/7118174/"
mylist = []

for i in range(1,4):
	url = prefix_url + str(i)
	resp = urllib.request.urlopen(url)
	html = resp.read().decode('utf-8')
	x = re.findall(r'<a href="/gl486546/article/details/(.+)">[\r\n]+\s*([\s\S]+?)\s*[\r\n]*</a>',html)
	print(len(x))
	for e in x:
		mylist.append(list(e))

mylist.sort(key=lambda x:x[1])
print("total = %d"%(len(mylist)))
with open('a.txt','w',encoding='utf-8') as f:
	for e in mylist:
		url_line = '[' + e[1] + '](http://blog.csdn.net/gl486546/article/details/' + e[0] + ')\n'
		f.write(url_line)

os.startfile('a.txt')
