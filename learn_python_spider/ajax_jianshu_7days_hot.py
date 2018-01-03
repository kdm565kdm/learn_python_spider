import urllib.request
from lxml import etree
import re
import json
import csv

fp = open('E:/spider/7d.csv','wt',newline='',encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('author','article','date','word','view','comment','like','gain','include'))
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
main_url = 'https://www.jianshu.com'
path = ''
def get_url(url):
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    html_code = html.decode('utf-8')
    selector = etree.HTML(html_code)
    infos = selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        href = info.xpath('a/@href')
        perfect_href = main_url+href[0]
        get_details(perfect_href)

def get_details(url):
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    html_code = html.decode('utf-8')
    selector = etree.HTML(html_code)
    author = selector.xpath('//span[@class="name"]/a/text()')[0]
    article = selector.xpath('//h1[@class="title"]/text()')[0]
    date = selector.xpath('//span[@class="publish-time"]/text()')[0]
    word = selector.xpath('//span[@class="wordage"]/text()')[0]
    view = re.findall('"views_count":(.*?),',html_code,re.S)[0]
    comment = re.findall('"comments_count":(.*?),',html_code,re.S)[0]
    like = re.findall('"likes_count":(.*?),',html_code,re.S)[0]
    id = re.findall('"id":(.*?),',html_code,re.S)[0]
    gain = re.findall('"total_rewards_count":(.*?),',html_code,re.S)[0]
    include_list = []
    include_urls = ['https://www.jianshu.com/notes/{}/included_collections?page={}'.format(id,str(i))
                    for i in range(1,10)]
    for include_url in include_urls:
        json_data = {"collections":[{"id":506695,"slug":"074e475b2f45","title":"成长励志","avatar":"http://upload.jianshu.io/collections/images/506695/VCG41678819337.jpg","owner_name":"简书"},{"id":25920,"slug":"f6b4ca4bb891","title":"生活家","avatar":"http://upload.jianshu.io/collections/images/25920/enhanced-buzz-wide-16461-1372163238-8.jpg","owner_name":"简书"},{"id":47,"slug":"bDHhpK","title":"首页投稿","avatar":"http://upload.jianshu.io/collections/images/47/%E9%A6%96%E9%A1%B5%E6%8A%95%E7%A8%BF.png","owner_name":"简书"},{"id":276392,"slug":"97becab9817a","title":"书单","avatar":"http://upload.jianshu.io/collections/images/276392/%E4%B9%A6%E5%8D%95.jpg","owner_name":"简书"},{"id":4,"slug":"yD9GAd","title":"读书","avatar":"http://upload.jianshu.io/collections/images/4/sy_20091020135145113016.jpg","owner_name":"简书"},{"id":553817,"slug":"36e5dce119fb","title":"learn","avatar":"http://upload.jianshu.io/collections/images/553817/bxe13cw29okd0ng4!1200.jpg","owner_name":"enjoyer_子非鱼"},{"id":258327,"slug":"85c0ead70e62","title":"书","avatar":"http://upload.jianshu.io/collections/images/258327/android.graphics.Bitmap_21071e58.jpeg","owner_name":"tuhtuh8"}],"page":1,"total_pages":8}
        includes = json_data['collections']
        for include in includes:
            include_title = include['title']
        
            include_list.append(include_title)
            
    info ={
        'author':author,
        'article':article,
        'date':date,
        'word':word,
        'view':view,
        'comment':comment,
        'like':like,
        'gain':gain,
        'include':include_list
    }
    print(info)
    writer.writerow((author,article,date,word,view,comment,like,gain,include_list))
def get_topics(url):
    #print(url)
    #req = urllib.request.Request(url=url,headers=headers)
    #res = urllib.request.urlopen(req).read()
    #html = res.read()
    json_data = {"collections":[{"id":506695,"slug":"074e475b2f45","title":"成长励志","avatar":"http://upload.jianshu.io/collections/images/506695/VCG41678819337.jpg","owner_name":"简书"},{"id":25920,"slug":"f6b4ca4bb891","title":"生活家","avatar":"http://upload.jianshu.io/collections/images/25920/enhanced-buzz-wide-16461-1372163238-8.jpg","owner_name":"简书"},{"id":47,"slug":"bDHhpK","title":"首页投稿","avatar":"http://upload.jianshu.io/collections/images/47/%E9%A6%96%E9%A1%B5%E6%8A%95%E7%A8%BF.png","owner_name":"简书"},{"id":276392,"slug":"97becab9817a","title":"书单","avatar":"http://upload.jianshu.io/collections/images/276392/%E4%B9%A6%E5%8D%95.jpg","owner_name":"简书"},{"id":4,"slug":"yD9GAd","title":"读书","avatar":"http://upload.jianshu.io/collections/images/4/sy_20091020135145113016.jpg","owner_name":"简书"},{"id":553817,"slug":"36e5dce119fb","title":"learn","avatar":"http://upload.jianshu.io/collections/images/553817/bxe13cw29okd0ng4!1200.jpg","owner_name":"enjoyer_子非鱼"},{"id":258327,"slug":"85c0ead70e62","title":"书","avatar":"http://upload.jianshu.io/collections/images/258327/android.graphics.Bitmap_21071e58.jpeg","owner_name":"tuhtuh8"}],"page":1,"total_pages":8}
    includes = json_data['collections']
    for include in includes:
        include_title = include['title']
        print(include_title)
urls = ['https://www.jianshu.com/trending/weekly?page={}'.format(str(i))
        for i in range(0,10)]


for url in urls:
    get_url(url)
