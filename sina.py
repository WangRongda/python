import urllib
import urllib2
import re
import sys
requrl="http://weibo.com/aj/v6/like/objectlike?ajwvr=6"

h = {
		'Cookie':'SINAGLOBAL=4717483517360.497.1470567601122; wvr=6; UOR=,,sports.ifeng.com; YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; login_sid_t=41513e188e55cc50470f71d98c3b5e0f; YF-V5-G0=d8809959b4934ec568534d2b6c204def; WBStore=ab2489e83fd8587e|undefined; _s_tentry=-; Apache=1733976713252.7495.1471751766461; ULV=1471751766514:7:7:1:1733976713252.7495.1471751766461:1471494484252; SCF=Aqzu23DY-VJ9lwtmiJMg-PuFgAcTMsE6JdZ-EgQj1bzhtlFB4ELPpOBQanF2tFNmC4NAFT9ncc_VajuYbM7KPzc.; SUB=_2A256vVbHDeTxGeVI6VcU9CbMyziIHXVZy88PrDV8PUNbmtBeLXnakW9zXvfQcHVpeEtvJ-FDrlHMpa8h4g..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhKgEafCdMiCg888eRaFbV.5JpX5K2hUgL.Foeceo-fShn7ehB2dJLoI0YLxK-L1hnL1KMLxK.L1KnLBo-LxK-L1-eLBKnLxK-L1h.L12BLxKML1-2L1hBLxKBLB.eLBK5LxKnLB-qLBoBt; SUHB=00x5QxEEfjksly; ALF=1503287830; SSOLoginState=1471751832; un=123899696@qq.com; YF-Page-G0=3d55e26bde550ac7b0d32a2ad7d6fa53', 
		'Referer':'http://weibo.com/u/3625548004/home?wvr=5',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
	}
test_data = { 'location':'v6_content_home','group_source':'group_all','rid':'0_0_1_2666927756016819420','object_id':'4010880066887262','object_type':'comment' }
test_data_urlencode = urllib.urlencode(test_data)
#print test_data_urlencode

req = urllib2.Request(url = requrl,headers=h,data =test_data_urlencode)
res_data = urllib2.urlopen(req)
res = res_data.read()
print res
