import urllib.request
import re
import time
from lxml import etree
import pymysql

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}

urls = ['https://movie.douban.com/top250?start={}'.format(str(i))
        for i in range(0,100,25)]

conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='mydb',port=3306,charset='utf8')
cursor = conn.cursor()
def get_detail_url(url):
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    html_code = html.decode('utf-8')
    selector = etree.HTML(html_code)
    detail_pages = selector.xpath('//div[@class="item"]/div[2]/div/a/@href')
    for page in detail_pages:
        get_info(page)


def get_info(url):
    try:
        req = urllib.request.Request(url,headers=headers)
        res = urllib.request.urlopen(req)
    except :
        return False
    html = res.read()
    html_code = html.decode('utf-8')
    selector = etree.HTML(html_code)
    name = selector.xpath('//div[@id="content"]/h1/span[1]/text()')[0]
    director = selector.xpath('//div[@id="info"]/span[1]/span[2]/a/text()')[0]
    actors = selector.xpath('//*[@id="info"]/span[3]/span[2]')[0]
    actor = actors.xpath('string(.)')
    style = re.findall('<span property="v:genre">(.*?)</span>',html_code,re.S)[0]
    #country = re.findall('<span class="p1">制片国家/地区:</span>(.*?)<br/>',html_code,re.S)[0]
    country = selector.xpath('//*[@id="info"]/span[8]/text()')[0]
    release_time = selector.xpath('//*[@id="info"]/span[10]/text()')[0]
    #time = re.findall('<span class="p1">片长:</span>.*?>(.*?)</span>',html_code,re.S)[0]
    time = re.findall('片长:</span>.*?>(.*?)</span>',html_code,re.S)[0]
    score = selector.xpath('//div[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]

    cursor.execute(
        "insert into doubanmovie (name,director,actor,style,country,release_time,time,score) value(%s,%s,%s,%s,%s,%s,%s,%s)",
        (str(name),str(director),str(actor),str(style),str(country),str(release_time),str(time),str(score))
        )
if __name__ == "__main__":
    for url in urls:
        get_detail_url(url)
        print(url)
        time.sleep(1)
    conn.commit()
