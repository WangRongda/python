#coding=utf-8
import urllib
import urllib2
import re
import sys
import time


requrl="http://szb.qzwb.com/dnzb/"
referer = ""
h = {
		'Host':'szb.qzwb.com',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36',
		'Referer': referer	
		}
def getHtml(requrl, h):
	req = urllib2.Request(url = requrl, headers = h)
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	return res
def regex(before, rule):
	reg = re.compile(rule, re.M)
	after = reg.findall(before)
	return after
def getDongnanURL(requrl, h) : #click Dongnanzaobao and get Dongnan url
	res = getHtml(requrl, h)
	c = regex(res, r'(?<=URL=)[^"]*')
	requrl += c[0]
	#print("Dongnan url = " + requrl)
	return requrl
def getRootURL(requrl):
	rootUrl = regex(requrl, r'^.*/')
	rootUrl = regex(rootUrl[0], r'^.*(?=/$)')
	#print("root url = " + rootUrl[0])
	return rootUrl[0]
def getLastDir(requrl):
	lastDir = regex(requrl, r'/[^/]*$')
	#print("lastDir = " + lastDir[0])
	return lastDir[0]
def getLastDate(rootUrl):
	lastdate = regex(rootUrl, r'2016.*$')
	#print("LastModifiedDate = " + lastdate[0])
	return lastdate[0] #2016-09/30
def changeDate(newDate):  #format : r'2016-09/30'
	newRootUrl = requrl + 'html/' + newDate  
	#print("newRootUrl = " + newRootUrl)
	return newRootUrl	

def getGongfuURL(requrl, h): #open Dongnanzaobao and get Gongfu url
	res = getHtml(requrl, h)
	url = regex(res, r'<[^<]*?(?=功夫早茶)')
	if url:
		url = regex(url[0], r'(?<=href=)[^>]*')
		#print("congfu url = " + url[0])
		return url[0]
	else:
		print("<p>" + date + " 没有功夫早茶</p>")
		print("<p>不信自己看: <a href='" + requrl + "'>" + requrl + "</a></p>")
		quit()

def getImgUrl(requrl, h): #open congfu url and get img url
	res = getHtml(requrl, h)
	Iurl = regex(res, r'<Area[^>]*>')
	n = 0
	url = range(10)
	for u in Iurl:
		temp = regex(u, r'(?<=href=")[^"]*')
		url[n] = temp[0]
		url[n] = rootUrl + '/' + url[n]
		n = n + 1
	return url
		
def getImg(requrl, h):
	res = getHtml(requrl, h)
	img = regex(res, r'(?<=<TD><IMG src=")[^"]*')
	if img:
		#print img[0]
		title = regex(res, r'(?<=<td class="font01" align=center style="color: #000000;">)[^<]*')
		print("<h1>" + title[0] + "</h1>")
		print("<p>date = " + date + "</p>")
		return img[0]
	else:
		return 
def GetNowTime():
	    return time.strftime("%Y-%m-%d",time.localtime(time.time()))
def isToday(lastDate):
	a = GetNowTime()
	today = time.strptime(a, "%Y-%m-%d")
	last = time.strptime(lastDate, "%Y-%m/%d")
	toStamp = int(time.mktime(today))
	laStamp = int(time.mktime(last))
	#print(toStamp)
	#print(laStamp)
	if laStamp < toStamp:
		print("<p>现在还没有今天的东南早报(" + a + ")</p>\n<p>最近的一期是：" + lastDate + "</p>")
	else:
		print("<p>今天(" + lastDate + "):</p>")

DFRequrl = getDongnanURL(requrl, h)
rootUrl = getRootURL(DFRequrl)
lastDate = getLastDate(rootUrl)

if len(sys.argv) != 1: # 2016/09/01
	date = sys.argv[1]
	d = list(date)
	d[4] = '-'
	date = ''.join(d)
	rootUrl = changeDate(date)
	DFRequrl = rootUrl + getLastDir(DFRequrl)
	#print("newDFurl = " + DFRequrl)
else:
	isToday(lastDate)
	date = lastDate

referer = requrl
congfuUrl = getGongfuURL(DFRequrl, h)
congfuUrl = rootUrl + '/' + congfuUrl
referer = DFRequrl
imgUrl = getImgUrl(congfuUrl, h)
referer = congfuUrl
for item in imgUrl:
	img = getImg(item, h)
	if img:
		sourceUrl = item
		break
if img:
	img = rootUrl + '/' + img
	print("<img style='display:block;' src='" + img + "'/>")
	print("<p>原链接：<a href='" + sourceUrl + "'>" + sourceUrl + "</a></p>")
else:
	print("<p>功夫早茶面板里面找不到图片</p>")
