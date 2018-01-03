import urllib.request
import re
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}

f = open('E:/spider/doupo.txt','a+')

def get_info(url):
    req = urllib.request.Request(url=url,headers=headers)
    try:
        res = urllib.request.urlopen(req)
    except:
        print('error')
        return False
    status = res.getcode()
    if status == 200:
        print(status)
        html = res.read()
        html_code=html.decode('utf-8')
        reg = r'<p>(.*?)</p>'
        contents = re.findall(reg,html_code,re.S)
        for content in contents:
            f.write(content+'\n')
    


if __name__ == '__main__':
    
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format
            (str(i)) for i in range(2,1665)]
    for url in urls:
        print(url)
        get_info(url)
        time.sleep(1)
    f.close()
