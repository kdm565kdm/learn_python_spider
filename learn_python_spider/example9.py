import urllib.request
from lxml import etree
import re
import time
#import pymongo

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
#client = pymongo.MongoClient('localhost',27017)
#mydb = client('mydb')
#musictop = mydb['musictop']
urls = ['https://music.douban.com/top250?start={}'.format(str(i))
        for i in range(0,50,25)]

fp = open('E:/spider/tem.txt','w+')
def get_detail_page(url):
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    html_code=html.decode('utf-8')
    selector = etree.HTML(html_code)
    detail_pages = selector.xpath('//a[@class="nbg"]/@href')
    for page in detail_pages:
        
        get_detail_info(page)
    
def get_detail_info(url):
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    html_code=html.decode('utf-8')
    selector = etree.HTML(html_code)
    song_name = selector.xpath('//div[@id="wrapper"]/h1/span/text()')[0]
    author = re.findall('表演者:.*?>(.*?)</a>',html_code,re.S)[0]
    styles = re.findall('<span class="p1">流派:<span>&nbsp;(.*?)<br>',html_code,re.S)
    if len(styles) == 0:
        style = '未知'
    else:
        style = styles[0].strip()
    time = re.findall('发行时间:</span>&nbsp;(.*?)<br />',html_code,re.S)[0].strip()

    publishers = re.findall('<span class="p1">出版者:</span>&nbsp;(.*?)<br>',html_code,re.S)
    if len(publishers) == 0:
        publisher = '未知'
    else:
        publisher = publishers[0].strip()
    score = selector.xpath('//div[@id="interest_sectl"]/div/div[2]/strong/text()')[0]
    info = {
        'song_name':song_name,
        'author':author,
        'style':style,
        'time':time,
        'publisher':publisher,
        'score':score
        }
    #musictop.insert_one(info)
    fp.write(author)
    fp.write('\n')
   

if __name__ == '__main__':
    for url in urls:
        get_detail_page(url)
        time.sleep(1)

    fp.close()
