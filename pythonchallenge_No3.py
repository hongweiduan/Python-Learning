from bs4 import BeautifulSoup  
import urllib2
import re
import sys
class find_the_number(object):
	"""docstring for find_the_number"""
	def __init__(self):
		super(find_the_number, self).__init__()
	def get_next_url(self,url):
		self.url = url
		# user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
		# x_req='XMLHttpRequest'
		# header = {"User-Agent": user_agent,'X-Requested-With':x_req}
		# req = urllib2.Request(url=self.url,headers=header)
		# 32839  ----653
		# 56881  ----2496
		# 16055  ----2507 66831   16044   68694
		content = urllib2.urlopen(self.url,timeout=100).read()
		print content
		# print content.find("nothing is")
		if not content.find("nothing is")==-1:
			# next_nothing = re.sub(r"nothing is \d",content)
			next_nothing = re.sub("\D","",content)
			print next_nothing
			next_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(next_nothing)
			# return self.get_next_url(next_url)
			return next_url
		elif not content.find("Yes.")==-1:
			print content
			# next_nothing = re.sub("\D","",content)
			next_nothing = re.sub("\D","",url)
			next_nothing = int(next_nothing)/2	
			print next_nothing
			# next_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044'
			# next_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(next_nothing/2)			
			next_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='			
			return next_url
		else:
			# next_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044'
			print content
			return "Got it"
next_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
c = find_the_number()
i = 0 
while 1:
	# print(next_url)
	next_url = c.get_next_url(next_url)
	if next_url=="Got it":
		print "^^^^^^^^"
		sys.exit()
	i += 1
	print("the "+str(i)+" times try!!!")

		