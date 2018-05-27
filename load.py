import  urllib.request
import re
import os
url = r'http://scp-wiki-cn.wikidot.com/'
scpid = input()
url += scpid
res = urllib.request.urlopen(url)
html = res.read().decode('utf-8')
#print(html)

dr = re.compile(r'<[^>]+>',re.S)
dd = dr.sub('',html)
print(dd)


logpath='D:/scp_log/'
if not os.path.exists(logpath):
    os.mkdir(logpath)
scplog = open(logpath+scpid+'.html','w',encoding='utf-8')
scplog.write(html)
scplog.close()