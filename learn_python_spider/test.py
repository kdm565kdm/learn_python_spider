from lxml import etree
import urllib.request,re

def getHtml(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    #print(res.getCode())
    html = res.read()
    return html


html = getHtml('http://www.baidu.com')
html=html.decode('utf-8')

#selector = etree.HTML(html)

#x=0
#data = selector.xpath('//div[@id="center_box"]/img/@src')
#info = data.xpath('string(.)')


#for each in data:
    #content = 'http://www.daniugeliuxining.com/'+each.replace('\n', '').replace(' ','').replace('\r','')
    #urllib.request.urlretrieve(content,'m/%s.jpg'%x)
    #print(each)
    #x = x+1
