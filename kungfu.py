import urllib
import urllib2
import re
#import sys
import json
#reload(sys)
#sys.setdefaultencoding('utf-8')
requrl="http://szb.qzwb.com/dnzb"
h = {
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36"
		}
req = urllib2.Request(url = requrl,headers = h)
res_data = urllib2.urlopen(req)
res = res_data.read()
print res
#m = re.compile(r'<ul id="live-list-contentbox[\s\S]*?<script', re.M)
#n = m.findall(res)
#a = re.compile(r'(?<=<a href=")[^"]*', re.M)
#href = a.findall(n[0])
#b = re.compile(r'(?<=title=")[^"]*', re.M)
#title = b.findall(n[0])
#i = 0
#for item in title:
#	print "================================================"
#	print ""
#	print item,
#	print href[i].replace('/','http://www.douyu.com/')
#	i = i+1
