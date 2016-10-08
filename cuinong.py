import urllib
import urllib2
import re
import sys
#test_data = {'encode':'gbk','callback':'jQuery1720908038619291107_1471085734309', 'voteId':'585', 'optionIds':'3655', 'uid':'0', '_':'1471086152477'}
#test_data_urlencode = urllib.urlencode(test_data)
requrl="http://changyan.sohu.com/api/2/comment/action?client_id=cyqyBluaj&topic_id=1523009909&comment_id=1123796978&action_type=1&callback=jQuery17204883733305069349_1471751504441&_=1471751583735"
req = urllib2.Request(url = requrl)

while 1:
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	print res

