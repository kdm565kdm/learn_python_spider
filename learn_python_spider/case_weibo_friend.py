from urllib import request
from urllib import parse
import json

headers = {
    'Cookie':'_T_WM=33daf456171587d4553d73b862cd0432; TMPTOKEN=jG5m7PBCkqfoG5JLEij3194XDlw9IXaatLAIsBhHS0nel4MCQXqd1iegNmJsmwi7; SUB=_2A253TZQ9DeRhGeVP61sU9S7Fwz2IHXVUsTx1rDV6PUJbkdBeLRKhkW1NTUhcAy050srTnhHkzRbrwLBcojIOrpC0; SUHB=0qjEGaitW45bwv; SCF=Al9_WTOOdwM3Mg4IvBcNFWWMeGCcrUyiyu-UmRbNv2GsmsYsJKzvJDxoWK44l9bu2jkO-lm-qt5v2VW_uKvp4MY.; SSOLoginState=1514792046; M_WEIBOCN_PARAMS=luicode%3D20000174%26lfid%3Dhotword%26featurecode%3D20000320%26uicode%3D20000318; H5_INDEX=0_friend; H5_INDEX_TITLE=%E5%A5%BD%E5%8F%8B%E5%9C%88%20',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Connection':'keep-alive'
    }

f= open('E:/spider/weibo_friends.txt','a+',encoding='utf-8')

def get_info(url,page):
    req = request.Request(url=url,headers=headers)
    res = request.urlopen(req)
    html = res.read()
    json_data = json.loads(html)
    card_groups = json_data[0]['card_group']
    for card_group in card_groups:
        f.write(card_group['mblog']['text'].split(' ')[0]+'\n')
    next_cursor = json_data[0]['next_cursor']

    if page<50:
        next_url = 'https://m.weibo.cn/index/friends?format=cards&next_cursor='+str(next_cursor)+'&page=1'
        print(next_cursor)#418925787205967
        page = page + 1
        get_info(next_url,page)
    else:
        f.close()
        return False

if __name__ == '__main__':
    url = 'https://m.weibo.cn/index/friends?format=cards'
    get_info(url,1)
    print('success')
