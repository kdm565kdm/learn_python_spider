import urllib.request
import urllib.parse
import json
import time
headers = {
    'Cookie':'JSESSIONID=ABAAABAAADEAAFICA5A25C76AF909372908DEE349F04A6F; _ga=GA1.2.2147202806.1514787674; _gid=GA1.2.825907251.1514787674; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1514787674; user_trace_token=20180101140249-655c99d1-eeb9-11e7-9fc4-5254005c3644; LGSID=20180101140249-655c9b8a-eeb9-11e7-9fc4-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20180101140249-655c9d0a-eeb9-11e7-9fc4-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; SEARCH_ID=f4e41771cc264f69a0b85123067fce2c; TG-TRACK-CODE=search_code; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1514787788; LGRID=20180101140443-a939b3a7-eeb9-11e7-9fc4-5254005c3644'
    ,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Connection':'keep-alive'
}

def get_page(url,params):
    data = urllib.parse.urlencode(params).encode('utf-8')
    req = urllib.request.Request(url=url,headers=headers,data=data)
    res = urllib.request.urlopen(req)
    html = res.read()
    json_data = json.loads(html)
    total_Count = json_data['content']['positionResult']['totalCount']
    page_number = int(total_Count/15) if int(total_Count/15)<30 else 30
    get_info(url,page_number)

def get_info(url,pages):
    for pn in range(1,page+1):
        params = {
            'first':'true',
            'pn':str(pn),
            'kd':'python'
            }
        data = urllib.parse.urlencode(params).encode('utf-8')
        req = urllib.request.Request(url=url,headers=headers,data=data)
        res = urllib.request.urlopen(req)
        html = res.read()
        json_data = json.loads(html)
        results = json_data['content']['positionResult']['result']
        for result in results:
            businessZones = result['businessZones']
            city = result['city']
            

if __name__ == '__main__':
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    params = {
        'first':'true',
            'pn':'1',
    'kd':'python'
        }
    get_page(url,params)
