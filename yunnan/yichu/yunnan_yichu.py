# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:07:07 2017

@author: liuxinyu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 15:07:31 2017

@author: liuxinyu
"""

import requests
import time 
page_list=list(range(1,7525))

url_front='http://yn.gsxt.gov.cn/notice/search/GET/announce?type=0102&mode=all&pageNo='
url_end='&areaId=&keyword='

detail_front='http://yn.gsxt.gov.cn/notice/'

#page_no=1

for page_no in page_list:
    url=url_front+str(page_no)+url_end   
                     
    try:
        res=requests.get(url,timeout=10)
        print('status:'+str(res.status_code))
    except:
        print('error_request:'+url)
        f = open ('yunan_error_yichu.txt','a')
        f.write('error page_no:'+str(page_no)+','+url+'\n')
        f.close    
    
    try:        
        result_json=res.json()
#    print(result_json)
        item_no=len(result_json['result']['data'])
        fl = open ('yunnan_yichu.txt','a')
        for i in list(range(0,item_no)):
            eptName=result_json['result']['data'][i]['etpName']
            link=result_json['result']['data'][i]['link']
            link=detail_front+link
            fl.write(eptName+','+link+'\n')
        fl.close
    except:
        print('error_json:'+url)
        f = open ('yunan_error_yichu.txt','a')
        f.write('error page_no:'+str(page_no)+','+url+'\n')
        f.close    
    print(str(page_no))
    time.sleep(2)
    
    
    
#    print(test1)
##
###etpName=test1.encode('utf-8')
##test2=test1.encode('utf-8')
##print(test2)
#
#
#fl = open ('unicode_test2.txt','a')
#fl.write(test1+'\n')
#fl.close

