#coding:utf-8
import aiml
import os
import urllib2
import urllib
# import urllib.request
import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
'''
request = urllib.request.urlopen('http://placekitten.com/g/2100/3200')
cat_img =request.read()

with open('cat_500_600.jpg','wb') as f:
	f.write(cat_img)
'''

def youdao_translater(need_translation_str):
	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
	data = {}
	data['type'] ='AUTO'
	data['i'] = need_translation_str
	data['doctype'] = 'json'
	data['xmlVersion'] = '1.6'
	data['keyfrom'] = 'fanyi.web'
	data['ue'] = 'UTF-8'
	data['typoResult'] = 'ture'
	#data = urllib.urlencode(data).encode('utf-8')
	data = urllib.urlencode(data)
    #data = urllib.urlencode(data)

	#response = urllib.request.urlopen(url,data)
	response = urllib2.urlopen(url,data)
	#html = response.read().decode('utf-8')
	html = response.read()

	#print(html)
	html_dic = json.loads(html)
	translated_str = html_dic['translateResult'][0][0]['tgt']
	return translated_str

os.chdir('/Users/Howie/Documents/potential-octo-garbanzo/alice')
alice = aiml.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')

while 1:
	ret = raw_input("I:")
	#ret = youdao_translater(ret)
	#print('Debug input str::'+ret)
	res = alice.respond(ret)
	#print('Debug output str::'+res)
	#res = youdao_translater(res)
	print("Robot:"+res)
