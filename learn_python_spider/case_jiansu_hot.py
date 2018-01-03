import urllib.request
from lxml import etree
from multiprocessing import Pool
import pymysql

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='mydb', port=3306, charset='utf8')
cursor = conn.cursor()
def get_info(url):
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    html_code = html.decode('utf-8')
    selector = etree.HTML(html_code)
    infos = selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        author = info.xpath('div/div[1]/div/a/text()')[0]
        time = info.xpath('div/div[1]/div/span/@data-shared-at')[0]
        title = info.xpath('div/a/text()')[0]
        content = info.xpath('div/p/text()')[0].strip()
        view = info.xpath('div/div[2]/a[1]/text()')[1].strip()
        comment = info.xpath('div/div[2]/a[2]/text()')[1].strip()
        like = info.xpath('div/div[2]/span[1]/text()')[0].strip()
        rewards = info.xpath('div/div[2]/span[2]/text()')

        if len(rewards) == 0:
            reward = '空'
        else:
            reward = rewards[0].strip()

        data = {
            'author':author,
            'time':time,
            'title':title,
            'content':content,
            'view':view,
            'comment':comment,
            'like':like,
            'reward':reward
            }
        print(1)
        


urls = ['https://www.jianshu.com/c/bDHhpK?order_by=commented_at&page={}'.format(str(i))
            for i in range(1,3)]
pool = Pool(4)
pool.map(get_info,urls)

