import urllib.request
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
def get_time_info(url,page):
    user_id = url.split('/')
    user_id = user_id[4]
    user_id = user_id.split('?')
    user_id = user_id[0]
    
    if url.find('page='):
        page = page+1
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    html_code = html.decode('utf-8')
    selector = etree.HTML(html_code)
    infos = selector.xpath('//div[@class="info"]')
    for info in infos:
        time = info.xpath('span/@data-shared-at')
        if len(time) != 0:
            print(time)
        
    #if page == 10:
        #print('a')
        #return False
    if len(time) == 0:
            return False
    next_url = 'https://www.jianshu.com/u/%s?order_by=shared_at&page=%s' % (user_id,page)
    print(next_url)
    get_time_info(next_url,page)



get_time_info('https://www.jianshu.com/u/9104ebf5e177?order_by=shared_at&page=',1)
