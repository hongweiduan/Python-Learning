# coding:utf-8
# import urllib.request
import re

text = 'al,,d,a,cas'
text_tab = text.split(",")
text_tab2 = re.split(",+",text,maxsplit=2)
for x in text_tab2:
	print x

pattern = re.compile(r'\*([^\*]+)\*')
input_str = 'Hello,*world*!'
output_str = re.sub(pattern,r'<em>\1<em>',input_str)
print(output_str)

pattern = re.compile(r'([a-z]+)\,\*([^\*]+)\*')
input_str = 'Hello,*world*!'
output_str = re.sub(pattern,r'<em>\1</em>,',input_str)
print(output_str)
