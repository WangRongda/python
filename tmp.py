import re 
a = '\/9e\/fa\/9efab2399c7c560b34de477b9aa0a465.mp3","ph_other":"","parts":[{"part":"adj.","means":["\u666e\u901a\u7684","\u901a\u4fd7\u7684","[\u6570\u5b66]\u516c\u5171\u7684","\u5171\u6709\u7684"]}vaf],"means":["\u666e\u901a\u7684","\u901a\u4fd7\u7684","[\u6570\u5b66]\u516c\u5171\u7684","\u5171\u6709\u7684"]}vaf]'
part = re.compile(r'(?<="means":\[)[^\[\]]*((?'Open'\[)[^\[\]]*)+((?'-Open'\])[^\[\]]*)+(?(Open)(?!))(?=\])', re.M)
p = part.findall(a)
print p
