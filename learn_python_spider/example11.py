from multiprocessing import Pool
import urllib.request
from lxml import etree
import re
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i))
        for i in range(1,36)]

info_lists = []

def judgment_sex(class_name):
  if class_name == 'womenIcon':
      return '女'
  else:
      return  '男'
    
def re_scraper(url):
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    html_code = html.decode('utf-8')
    ids = re.findall('<h2>\n(.*?)\n</h2>',html_code,re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>',html_code,re.S)
    sexs = re.findall('<div class="articleGender (.*?)">',html_code,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',html_code,re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>',html_code,re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论',html_code,re.S)
    for id,level,sex,content,laugh,comment in zip(ids,levels,sexs,contents,laughs,comments):
        info = {
            'id':id,
            'level':level,
            'sex':judgment_sex(sex),
            'content':content,
            'laugh':laugh,
            'comment':comment
        }
        info_lists.append(info)
        
if __name__ == "__main__":
    start_1 = time.time()
    for url in urls:
        re_scraper(url)
    end_1 = time.time()
    print('串行爬虫：',end_1-start_1)
    start_2 = time.time()
    pool = Pool(processes=2)
    pool.map(re_scraper(),urls)
    end_2 = time.time()
    print('双线程：',end_2-start_2)
    start_3 = time.time()
    pool = Pool(processes=4)
    pool.map(re_scraper(),urls)
    end_3 = time.time()
    print('四线程：',end_3-start_3)
