import  urllib.request
import re
import os
def load_scp_database(scpid):
    url = r'http://scp-wiki-cn.wikidot.com/'
    url += scpid
    res = urllib.request.urlopen(url)
    html = res.read().decode('utf-8')
    scplog = open(logpath+scpid+'.html','w',encoding='utf-8')
    scplog.write(html)

    dr = re.compile(r'<[^>]+>',re.S)
    dd = dr.sub('',html)
    print(dd)
def batch_load(l,r):
    for i in range(l,r+1):
        load_scp_database('scp-'+str(i))

#url = r'http://scp-wiki-cn.wikidot.com/'
#scpid = input()
#url += scpid
#res = urllib.request.urlopen(url)
#html = res.read().decode('utf-8')
#print(html)
#dr = re.compile(r'<[^>]+>',re.S)
#dd = dr.sub('',html)
#print(dd)

logpath='D:/scp_log/'
if not os.path.exists(logpath):
    os.mkdir(logpath)
batch_load(1000,1100)
scp_id=input()
load_scp_database(scp_id)