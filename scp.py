import  urllib.request
import re
import os
logpath='D:/scp_log/'
welcome_word = "欢迎登陆SCiPNET直接存储终端。请输入口令"
FAIL_READ = 'READ_FAILED'
def create_log_folder(): # creates folder for the logs
    
    if not os.path.exists(logpath): 
        os.mkdir(logpath)

def get_scp(scpid): # gets SCP file from Internet
    url = 'http://scp-wiki-cn.wikidot.com/'
    url += scpid
    try:
        res = urllib.request.urlopen(url)
        html = res.read().decode('utf-8')
        return html
    except:
        print(scpid + 'Load FAILED!')
        return FAIL_READ    
    else:
        print(scpid + 'Load Success')
    
    
def batch_load(l,r):
    for i in range(l,r+1):
        get_scp('scp-'+str(i))

def output_raw_scp_file(html): # Output the main files, ignore the rest
    
    file_begin = '<div id="page-content">'
    file_end =   '<div class="page-tags">'
    pos1 = int(html.find(file_begin))
    pos2 = int(html.find(file_end))
    #print(pos1)
    #print(pos2)
    html = html[pos1:pos2]

    dr = re.compile(r'<[^>]+>',re.S)
    raw_document = dr.sub('',html)
    raw_document = raw_document.strip()
    print(raw_document)

def record_log(scpid,html):
    scplog = open(logpath+scpid+'.html','w',encoding='utf-8')
    scplog.write(html)
    scplog.close()

#main:
create_log_folder()
print(welcome_word)
while(1):
    inputLine = input() + ' '

    if(inputLine.find('access')==0):
        scp_id = inputLine[len('access')+1:inputLine.find(' ',len('access')+2)]
        print('Accessing '+scp_id+' ...')
        print('------------------------------')

        print(scp_id.upper())
        scp_html=get_scp(scp_id)
        if(scp_html==FAIL_READ):
            print('This SCP does not exist or denied access!')
        else:
            output_raw_scp_file(scp_html)
            record_log(scp_id,scp_html)

        print('------------------------------')

    if(inputLine.find('exit')==0):
        print("Exiting System.")
        break
