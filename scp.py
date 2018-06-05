import  urllib.request
import re
import os
import time
logpath='D:/scp_log/'
welcome_word = "欢迎登陆SCiPNET直接存储终端。请输入口令"
INTERVAL = '\n'+50*'-'+'\n'
FAIL_READ = 'READ_FAILED'
def get_kth_word(k,st): #get K-th word from a ' '(space) intervaled string 
    pos = 0
    for i in range(1,k):
        pos = st.find(' ',pos+1,len(st))
        
    pos2 = st.find(' ',pos+1,len(st))
   
    if(pos2 == -1):
        pos2 = len(st)
    if(pos != 0):
        pos += 1
    return st[pos:pos2]

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

def record_log(scpid,html): #log documents to Dir
    scplog = open(logpath+scpid+'.html','w',encoding='utf-8')
    scplog.write(html)
    scplog.close()

#main:
create_log_folder()
print(welcome_word)
while(1):
    inputLine = input() + ' '
    print(INTERVAL)
    
    if(get_kth_word(1,inputLine) == 'access'):
        scp_id = get_kth_word(2,inputLine)
        print('Accessing '+scp_id+' ...')
        
        print(scp_id.upper())

        scp_html=get_scp(scp_id)
        if(scp_html==FAIL_READ):
            print('This SCP does not exist or denied access!')
        else:
            output_raw_scp_file(scp_html)
            record_log(scp_id,scp_html)

    if(get_kth_word(1,inputLine) == 'batch'):
        lpos = int(get_kth_word(2,inputLine))
        rpos = int(get_kth_word(3,inputLine))
        batch_load(lpos,rpos)
    if(get_kth_word(1,inputLine) == 'exit'):
        print("Exiting System.")
        time.sleep(2)
        break
    print(INTERVAL)
