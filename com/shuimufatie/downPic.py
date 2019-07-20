from selenium import webdriver
import time
import urllib
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

'''
/html/body/section/section/div[3]/table/tbody/tr[1]/td[2]/a
/html/body/section/section/div[3]/table/tbody/tr[2]/td[2]/a
/html/body/section/section/div[3]/table/tbody/tr[30]/td[2]/a
/html/body/section/section/div[3]/table/tbody/tr[1]/td[2]/a

'''
b = webdriver.Firefox()
for j in range(520, 525):
    b.get("http://www.newsmth.net/nForum/#!board/MyPhoto?p=%s" % j)
    for i in range(1, 30, 1):
        print("-----   ", i)
        time.sleep(1)
        eles = b.find_element_by_xpath('/html/body/section/section/div[3]/table/tbody/tr[%s]/td[2]/a' % i)
        eles.click()
        time.sleep(20)
        eles1 = b.find_elements_by_class_name("resizeable")
        k = 0
        print(len(eles1))
        try:
            for img in eles1:
                print("       ------")
                zz = img.get_attribute("src")
                urllib.request.urlretrieve(zz, "i%s j%s k%s.png" % (i, j, k))
                k = k + 1
                time.sleep(20)
        except:
            pass
        k = 0
        time.sleep(5)
        b.back()
