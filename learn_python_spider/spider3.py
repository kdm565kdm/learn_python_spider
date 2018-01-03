from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import urllib.request
import json


def spider(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    html=html.decode('utf-8')
    selector = etree.HTML(html)
    #images =[]

    content_field = selector.xpath('//div[@id="center_box"]')
    print(content_field.xpath('string(.)'))
    for each in content_field:
        print('a')
        img_src = each.xpath('@src')[0].replace('&quot','')
        
        #images.append(img_src)
    return 'a'

if __name__ == "__main__":
    #pool=ThreadPool(2)
    f=open('content.txt', 'a')
    page = []
    
    for i in range(1, 38):
        newpage = 'http://manhua.dmzj.com/taobikechiquehenguanyong/58124.shtml#@page=' + str(i)
        page.append(newpage)

    for j in range(0, 1):
        p = page[j]
        f.writelines( spider(p)+'\n')
    f.close()
