from bs4 import BeautifulSoup
import urllib.request
import json
from selenium import webdriver

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
driver = webdriver.PhantomJS('phantomjs')

url_path = 'https://www.pexels.com/search/'

word = input('请输入您要下载的图片类型（由于调用不了思必客API，请输入英文）：')
url = url_path + word +'/'
driver.get(url)
html_code = driver.page_source
soup = BeautifulSoup(html_code, 'lxml')
imgs = soup.select('article > a > img')
list = []
for img in imgs:
    photo = img.get('src')
    list.append(photo)


path = 'E:/spider/photo'
for item in list:
    req = urllib.request.Request(url=item,headers=headers)
    res = urllib.request.urlopen(req)
    resource = res.read()
    fp.open(path+item.split('?')[0][-10:],'wb')
