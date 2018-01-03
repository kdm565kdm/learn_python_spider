import urllib.request
from bs4 import BeautifulSoup
import time
from selenium import webdriver
driver = webdriver.PhantomJS('phantomjs')

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
def get_links(url):
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    
    ranks = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')    
    titles =soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    times = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
 
    for rank, title, time in zip(ranks, titles, times):
        data = {
            'rank' : rank.get_text().strip(),
            'singer' : title.get_text().split('-')[0],
            'song' : title.get_text().split('-')[1],
            'time' : time.get_text().strip()
            }
        print(data)


if __name__ == '__main__':
    urls =['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in
           range(1,24)]

    for url in urls:
        print(url)
        get_links(url)
        time.sleep(1)
