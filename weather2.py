# -*- coding: UTF-8 -*-
import urllib
import urllib2
import json
import sys
import tree
if len(sys.argv)==1 :
	requrl="http://v.juhe.cn/weather/index?format=1&cityname=%E6%9D%AD%E5%B7%9E&key=2130ee503b9d41e4c58d976fa80e8bb3"
else:
	add = urllib.quote(sys.argv[1])
	requrl="http://v.juhe.cn/weather/index?format=1&cityname="+add+"&key=2130ee503b9d41e4c58d976fa80e8bb3"

req = urllib2.Request(url = requrl)
res_data = urllib2.urlopen(req)
res = res_data.read()
s = json.loads(res)
tree.print_tree(s)
