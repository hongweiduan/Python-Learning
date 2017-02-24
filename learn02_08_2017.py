import urllib.request
import json
import time
'''
request = urllib.request.urlopen('http://placekitten.com/g/2100/3200')
cat_img =request.read()

with open('cat_500_600.jpg','wb') as f:
	f.write(cat_img)
'''

while 1:
	need_translation_str = input("请输入需要翻译的内容（输入q退出）:\r\n")
	if need_translation_str == 'q':
		break

	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'

	data = {}
	data['type'] ='AUTO'
	data['i'] = need_translation_str
	data['doctype'] = 'json'
	data['xmlVersion'] = '1.6'
	data['keyfrom'] = 'fanyi.web'
	data['ue'] = 'UTF-8'
	data['typoResult'] = 'ture'
	data = urllib.parse.urlencode(data).encode('utf-8')

	response = urllib.request.urlopen(url,data)
	html = response.read().decode('utf-8')

	#print(html)
	html_dic = json.loads(html)
	translated_str = html_dic['translateResult'][0][0]['tgt']
	print('翻译结果为：%s'%translated_str)
	time.sleep(0.1)
