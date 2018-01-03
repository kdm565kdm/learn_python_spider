import urllib.request,re

def getHtml(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    return html

def getImg(url):
    html=getHtml(url)
    page=1
    x=0
    reg = r'<div.*?center_box.*?<img.*?src"(.*?)"'
    images=re.compile(reg,re.DOTALL)
    while page <= 38:
        if page == 1:
            a_html = html.decode('utf-8')
            imglist = re.findall(images,a_html)
            for imgurl in imglist:
                urllib.request.urlretrieve(imgurl,'m/%s.jpg'%x)
                x = x+1

        else:
            html=html
        page+=1
    

    


html=getImg("http://manhua.dmzj.com/taobikechiquehenguanyong/58124.shtml#@page=1")

