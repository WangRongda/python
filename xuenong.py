import urllib
import urllib2
import re
import sys
test_data = {'encode':'gbk','callback':'jQuery1720908038619291107_1471085734309', 'voteId':'585', 'optionIds':'3655', 'uid':'0', '_':'1471086152477'}
test_data_urlencode = urllib.urlencode(test_data)
requrl="http://score.my.tv.sohu.com/vote/voteOption.do"
req = urllib2.Request(url = requrl,data =test_data_urlencode)

dst = re.compile(r'(?<="num":)[^,]*', re.M)
while 1:
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	d = dst.findall(res)
	print d
	if (int(d[1]) - int(d[0])) > 73212:
		break

