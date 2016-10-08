import urllib
import urllib2
import re
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
requrl="http://www.douyu.com/member/cp/get_follow_list"
h = {
		"Cookie":"acf_devid=f0df277e5cf7f8811404dd846a5814b4; acf_auth_wl=; acf_usermsgnum3412135=0; acf_showtiprmd3412135=0; acf_boxtit=1; acf_giftAnchor=1; acf_shareplogin=3412135; PHPSESSID=a9im1ov6dav4uqbecp3f5haj92; acf_auth=e6cdWo41XbQPg2dq9mX4FT3bsrSXwQiU0lQKMNKTjBjj5efFyPmhZY22DxslfsdrD5ZxpmrtcblE0oBvfTaVxgfELEv10BXY6sf4SLa8dsrIbGf237cnCNs; wan_auth37wan=c7f283541068KTMZOWBP4Xn2tw%2Bv7F5WEiFOwTZJBoG2scIehEZ1czSlPQ8YW2Lzg64PFM1%2Fft8MGPFCnL7iPbo%2Bf4dS%2FFWg5wd%2FiAvrWpNo%2BTld; acf_uid=3412135; acf_username=qq_OQwlv9GK; acf_nickname=Tonbecx; acf_own_room=0; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_ltkid=44004684; acf_biz=1; acf_stk=825dec9190fdc5ed; acf_avatar=http%3A%2F%2Fuc.douyutv.com%2Fupload%2Favatar%2Fdefault%2F13_; _dys_page_refer2=2.5.2.2.5.2.5.2.5.2; acf_did=2F188E6304A048FEF5F1D4C3A0765944; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1462617419,1462688291,1462759206,1462765511; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1462778562; acf_userletnum3412135=0"
		}
req = urllib2.Request(url = requrl,headers = h)
res_data = urllib2.urlopen(req)
res = res_data.read()
print res
if res:
	encodedjson = json.loads(res)
	a = encodedjson['room_list']
	if a:
		for item in a:
			print item['room_name']
	else:
		print "no anchor"

