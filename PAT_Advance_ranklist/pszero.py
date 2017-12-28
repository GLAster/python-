import urllib.request
import re
import os

url="https://www.patest.cn/contests/pat-a-practise/ranklist?page="
data=[]

p = re.compile(r'[\s\S]+<tbody>(?P<tbody>[\s\S]+)</tbody>')

for i in range(1,20):
	ret = urllib.request.urlopen(url+str(i))
	html = ret.read().decode('utf-8')
	m = p.match(html)
	x = m.group('tbody')
	x = re.sub(r'\n|\r| ','',x)
	x = re.findall(r'<tr><td>(.+?)</td><td><ahref="/users/(.+?)">(.+?)</a></td>[\s\S]+?</tr>',x)
	if x:
		for e in x:
			data.append(list(e))


with open('rank.txt','w',encoding='utf-8') as f:
	for e in data:
		f.write(str(e)+'\n')

os.startfile('rank.txt')
