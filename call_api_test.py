#coding:utf-8
import aiml
import os
import urllib2
import urllib
import time
import os.path
# import urllib.request
import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_pic_url():
	my_key = '15b1a3dcd781d7c20c4f09d65fbda469'
	url1 = 'http://api.huceo.com/meinv/?key=%s&num=10' % my_key
	req = urllib2.Request(url1)
	resp= urllib2.urlopen(req)
	content =resp.read()
	if not content:
		error("No network -_-!")
	json_tab = json.loads(content)
	# pic_len = len(json_tab['newslist'])   #it is 10
	# print(pic_len)
	return json_tab
def get_work_path():
	work_path = os.getcwd()
	print(work_path)
	pic_path = work_path+'/picture'
	if os.path.exists(pic_path):
		print("--have it--")
	else:
		os.mkdir(pic_path)
	return pic_path

pic_path = get_work_path()
os.chdir(pic_path)
def save_pic(url,path):
	data = urllib2.urlopen(url)
	data = data.read()
	f = file(path,'wb')
	f.write(data)
	f.close()
# save_pic(r'http://image.hnol.net/c/2016-06/05/08/201606050820548311-5200043.jpg','1.jpg')
def save_all_pic(j):
	json_tab = get_pic_url()
	print(json_tab)
	for x in xrange(0,10):
		pic_url = json_tab['newslist'][x]['picUrl']
		name = json_tab['newslist'][x]['title']
		print(name)
		pics_path = str(name)+'.jpg'
		save_pic(pic_url,pics_path)

j = 1
while 1:
	save_all_pic(j)
	time.sleep(10)
	j+=1



# path = "me.jpg"  
# data = urllib.urlopen(url).read()  
# f = file(path,"wb")  
# f.write(data)  
# f.close()