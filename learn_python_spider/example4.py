import urllib.request
import re
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
file = open('E:/spider/qiushibaike.txt','a+')

info_lists = []

def judgment_sex(class_name):
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'
def get_info(url):
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    html_code=html.decode('utf-8')
    ids = re.findall('<h2>(.*?)</h2>',html_code,re.S)
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


if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i))
            for i in range(1,36)]

    for url in urls:
        get_info(url)

    for info_list in info_lists:
        try:
            file.write(info_list['id']+'\n')
            file.write(info_list['level']+'\n')
            file.write(info_list['sex']+'\n')
            file.write(info_list['content']+'\n')
            file.write(info_list['laugh']+'\n')
            file.write(info_list['comment']+'\n')
        except:
            break
    print('抓取完成')
    file.close()
