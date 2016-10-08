import urllib
import urllib2
import re
#import sys
import json
#reload(sys)
#sys.setdefaultencoding('utf-8')
requrl="http://www.douyu.com/directory/all"
h = {
		"Cookie":"acf_devid=f0df277e5cf7f8811404dd846a5814b4; acf_auth_wl=; acf_usermsgnum3412135=0; acf_auth=4338P484OrcgcN0pxcsjV%2Fl87lE1ChOTFvvOGQzUqFa%2FXyksn%2B76tftlHkkab0dxZiUnhwow16hOsCRqGBTokLsHII9L3T8YMemwqpAosgmUv67nwIpkv7c; wan_auth37wan=6d6876a0e519%2F%2BQ57ht%2BzR%2BzIEZJ0BO7wx6ePLz6n7XmNlQFx%2BKb9CGmwUTCdFs2kQoUhL1AszaSjuKFkwNoVh142egOohAStPWy1uoG4A2V3wvK; acf_uid=3412135; acf_username=qq_OQwlv9GK; acf_nickname=Tonbecx; acf_own_room=0; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_ltkid=44004684; acf_biz=1; acf_stk=4fe3a23710989d7b; acf_lastMayEnterTime=1462198757763; acf_avatar=http%3A//uc.douyutv.com/upload/avatar/default/13_; PHPSESSID=dsckmf2t16rer3usq5ril8vrj7; acf_boxtit=1; acf_did=2F188E6304A048FEF5F1D4C3A0765944; _dys_page_refer2=1.2.2.2.2; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1462066824,1462104560,1462152970,1462198757; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1462203323; acf_userletnum3412135=0",
		"Referer":"http://www.douyu.com/directory/all",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36"
		}
req = urllib2.Request(url = requrl,headers = h)
res_data = urllib2.urlopen(req)
res = res_data.read()
#print res
m = re.compile(r'<ul id="live-list-contentbox[\s\S]*?<script', re.M)
n = m.findall(res)
a = re.compile(r'(?<=<a href=")[^"]*', re.M)
href = a.findall(n[0])
b = re.compile(r'(?<=title=")[^"]*', re.M)
title = b.findall(n[0])
i = 0
for item in title:
	print "================================================"
	print ""
	print item,
	print href[i].replace('/','http://www.douyu.com/')
	i = i+1
