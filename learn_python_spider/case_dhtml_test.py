from selenium import webdriver
from lxml import etree
import urllib.request

driver = webdriver.PhantomJS('phantomjs')

def gethtml(url):
    driver.get(url)
    html = driver.page_source
    return html

def getImg(url):
    x = 0
    html = url
    for i in range(1,39,1):
        tem = html + str(i)
        html_source = gethtml(tem)
        selector = etree.HTML(html_source)
        data = selector.xpath('//div[@id="center_box"]/img/@src')
        for each in data:
            print(each)
            urllib.request.urlretrieve(each,'goddess/%s.jpg'%x)
            y = str(x)
            print('图片'+y+'.jpg已经保存到goddess文件夹')
            x = x+1
        print('\n')

url = 'http://manhua.dmzj.com/taobikechiquehenguanyong/58124.shtml#@page='
getImg(url)

