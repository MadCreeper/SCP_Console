import  urllib.request
import re
import os
logpath='D:/scp_log/'
def create_log_folder(): # creates folder for the logs
    
    if not os.path.exists(logpath): 
        os.mkdir(logpath)

def get_scp(scpid): # gets SCP file from Internet
    url = r'http://scp-wiki-cn.wikidot.com/'
    url += scpid
    res = urllib.request.urlopen(url)
    html = res.read().decode('utf-8')
    return html
   
def output_raw_scp_file(html): # Output the main files, ignore the rest
    dr = re.compile(r'<[^>]+>',re.S)
    file_begin = '<div id="page-content">'
    file_end =   '<div class="page-tags">'
    pos1 = int(html.find(file_begin))
    pos2 = int(html.find(file_end))
    #print(pos1)
    #print(pos2)
    html = html[pos1:pos2]
    dd = dr.sub('',html)
    print(dd)

def record_log(scpid,html):
    scplog = open(logpath+scpid+'.html','w',encoding='utf-8')
    scplog.write(html)
    scplog.close()

#main:
create_log_folder()
while(1):
    inputLine = input() + ' '
    if(inputLine.find('access')==0):
        scp_id = inputLine[len('access')+1:inputLine.find(' ',len('access')+2)]
        print('Accessing'+scp_id+'...')
        
        scp_html=get_scp(scp_id)
        output_raw_scp_file(scp_html)
        record_log(scp_id,scp_html)

