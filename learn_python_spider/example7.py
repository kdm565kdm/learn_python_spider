import urllib.request
from lxml import etree
from selenium import webdriver

driver = webdriver.PhantomJS('phantomjs')
urls = ['http://jandan.net/ooxx/page-{}'.format(str(i))
        for i in range(0,20)]

path = 'E:/spider/煎蛋网/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
def get_photo(url):
    #req = urllib.request.Request(url=url,headers=headers)
    #res = urllib.request.urlopen(req)
    driver.get(url)
    #html = res.read()
    #html_code = html.decode('utf-8')
    html_code = driver.page_source
    selector = etree.HTML(html_code)
    photo_urls = selector.xpath('//p/a[@class="view_img_link"]/@href')
    for photo_url in photo_urls:
        whole_url = 'http:'+ photo_url
        req = urllib.request.Request(url=whole_url,headers=headers)
        res = urllib.request.urlopen(req)
        resource = res.read()
        #print(resource)
        fp = open(path + photo_url[-10:],'wb')
        fp.write(resource)
        fp.close()


get_photo('http://jandan.net/ooxx/page-1')
