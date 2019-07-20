
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ToBan:
    def toBankuai(name,b):
        time.sleep(3)
        elesearch = b.find_element_by_id("b_search")
        elesearch.clear()
        elesearch.send_keys(name)
        elesearch.send_keys(Keys.ENTER)
        time.sleep(5)

        return b
    def tiezi(title,context,b):
        elefabiao = b.find_element_by_xpath("/html/body/section/section/div[1]/div[2]/a[1]")
        elefabiao.click()
        time.sleep(5)
        eletitle = b.find_elements_by_xpath('//*[@id="post_subject"]')
        print(len(eletitle))
        eletext = b.find_elements_by_id("post_content")
    #elexuanze = b.find_elements_by_id("upload_select")
        elefabu = b.find_element_by_xpath('//*[@id="post_content"]')
        eletitle[0].click()
        eletitle[0].send_keys(title)
        eletext[0].click()
        eletext[0].send_keys(context)
        elefabu.submit()
        return b