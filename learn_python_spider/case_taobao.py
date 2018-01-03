from selenium import webdriver
from lxml import etree
import time

driver = webdriver.PhantomJS()
driver.maximize_window()
def get_info(url,page):
    page = page + 1
    driver.get(url)
    driver.implicitly_wait(10)
    selector = etree.HTML(driver.page_source)
    infos = selector.xpath('//div[@class="item J_MouserOnverReq  "]')
    for info in infos:
        data = info.xpath('div[2]/div/a')[0]
        goods = data.xpath('string()').strip()
        price = info.xpath('div[2]/div[1]/div[1]/strong/text()')[0]
        sell = info.xpath('div[2]/div[1]/div[2]/text()')[0]
        shop = info.xpath('div[2]/div[3]/div[@class="shop"]/a/span[2]/text()')[0]
        address = info.xpath('div[2]/div[3]/div[@class="location"]/text()')[0]

        commodity = {
            'good':goods,
            'price':price,
            'sell':sell,
            'shop':shop,
            'address':address
            }
        print(commodity)

    if page <= 15:
        Next_page(url,page)
    else:
        pass

def Next_page(url,page):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//a[@trace="srp_bottom_pagedown"]').click()
    time.sleep(4)
    driver.get(driver.current_url)
    driver.implicitly_wait(10)
    get_info(driver.current_url,page)

if __name__ == '__main__':
    page = 1
    url = 'https://www.taobao.com/'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_id('q').clear()
    driver.find_element_by_id('q').send_keys('男士短袖')
    driver.find_element_by_class_name('btn-search').click()
    get_info(driver.current_url,page)
