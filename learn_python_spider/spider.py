import urllib.request,re

def getHtml(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/63.0.3239.108 Safari/537.36'}
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    status = res.getcode()
    print(status)
    html = res.read()
    return html

def getImg(html):
    reg = r'<a.*?alt=".*?新垣结衣.*?".*?<img.*?data-original = "(.*?)"'
    images=re.compile(reg,re.DOTALL)
    html=html.decode('utf-8')
    imglist=re.findall(images,html)
    x=0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'images/%s.jpg'%x)
        x = x+1

    


html=getHtml("http://www.win4000.com/zt/xyjy.html")
#img=getImg(html)

