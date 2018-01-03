from selenium import webdriver
import time
import csv

driver = webdriver.PhantomJS()
driver.maximize_window()
f = open('E:/spider/qz.txt','a+', encoding='utf-8')

def get_info(qq):
    driver.get('https://user.qzone.qq.com/{}/311'.format(qq))
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False

    if a == True:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys('1476045903')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('kdm565')
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        b = True
    except:
        b = False

    if b == True:
        contents = driver.find_elements_by_css_selector('.content')
        times = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
        for content, tim in zip(contents, times):
            data = {
                'time':tim.text,
                'content':content.text
                }
            
            f.write(data+'\n')

if __name__ == '__main__':
    qq_lists = []
    fp = open('E:/chrome/QQmail (2).csv')
    reader = csv.DictReader(fp)
    for row in reader:
        qq_lists.append(row['电子邮件'].split('@')[0])
    fp.close()

    for item in qq_lists:
        get_info(item)
    f.close()

