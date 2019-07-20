from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys

'''
首先登录，将cookie存入，然后关闭浏览器。之后在打开另外一个
浏览器对象，将cookie存入新的浏览器，让浏览器搜索是否有“退出字样”
'''
url = "http://www.newsmth.net/"
ursname = "tortelee"
password = "lt19911218"


def test_cookie(url, usrname, password):
    b = webdriver.Firefox()
    b.get(url)
    eleUsr = b.find_element_by_id("id")
    elePw = b.find_element_by_id("pwd")
    eleClick = b.find_element_by_id("b_login")
    action = ActionChains(b)
    action.click(eleUsr)
    action.send_keys(usrname)
    action.click(elePw)
    action.send_keys(password)
    action.click(eleClick)
    action.perform()
    cookies = b.get_cookies()
    time.sleep(3)
    elesearch = b.find_element_by_id("b_search")
    elesearch.clear()
    elesearch.send_keys("华中科技大学")
    elesearch.send_keys(Keys.ENTER)
    time.sleep(5)
    elefabiao = b.find_element_by_xpath("/html/body/section/section/div[1]/div[2]/a[1]")
    elefabiao.click()
    time.sleep(5)
    eletitle = b.find_elements_by_xpath('//*[@id="post_subject"]')
    print(len(eletitle))
    eletext = b.find_elements_by_id("post_content")
    #elexuanze = b.find_elements_by_id("upload_select")
    elefabu = b.find_element_by_xpath('//*[@id="post_content"]')
    eletitle[0].click()
    eletitle[0].send_keys("测试")
    eletext[0].click()
    eletext[0].send_keys("这是一个测试")

    elefabu.submit()
    b.close()
    return 0

test_cookie(url,ursname,password)
