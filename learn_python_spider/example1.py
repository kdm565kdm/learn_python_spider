from bs4 import BeautifulSoup
import urllib.request
import time
from selenium import webdriver
driver = webdriver.PhantomJS('phantomjs')

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}

def judgement_sex(class_name):
    if class_name == ['member_girl_ico']:
        return '女'
    else:
        return '男'

def get_links(url):
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get("href")
        get_info(href)

def get_info(url):
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    soup = BeautifulSoup(html,'lxml')
    tittles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    address = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
    prices = soup.select('#pricePart > div.day_l > span')
    imgs = soup.select('#curBigImage')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')

    for tittle, address, price, img, name, sex in zip(tittles,address,prices,imgs,names,sexs):
        data = {
            'tittle':tittle.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text().strip(),
            'img':img.get("src"),
            'name':name.get_text(),
            'sex':judgment_sex(sex.get("class"))
            }
        print(1)
        print(data)

if __name__ == '__main__':
    urls =['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,14)]
    for single_url in urls:
        get_links(single_url)
        time.sleep(2)
