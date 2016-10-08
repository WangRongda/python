import urllib
import urllib2
import re
import sys
test_data = {'from':'en','to':'zh','query':sys.argv[1],'transtype':'realtime','simple_means_flag':'3'}
test_data_urlencode = urllib.urlencode(test_data)
test_data_urlencode = urllib.urlencode(test_data)
requrl="http://fanyi.baidu.com/v2transapi"
req = urllib2.Request(url = requrl,data =test_data_urlencode)
res_data = urllib2.urlopen(req)
res = res_data.read()
dst = re.compile(r'(?<=\[{"dst":")[^"]*', re.M)
part = re.compile(r'(?<={"part":")[^"]*', re.M)
means = re.compile(r'(?<=means":\[)[^\]]*',re.M)
d = dst.findall(res)
p = part.findall(res)
m = means.findall(res)
i = 0
print "												 "
print "================================================================"
print sys.argv[1]+" :",
print d[0].decode('unicode_escape')
print "-------"
for item in p:
	print item.decode('unicode_escape'),
	print m[i].decode('unicode_escape')
	i = i+1
print "================================================================"
print "												 "
