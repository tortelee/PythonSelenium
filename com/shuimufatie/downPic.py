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
/html/body/section/section/div[3]/table/tbody/tr[5]/td[2]/a
/html/body/section/section/div[3]/div[1]/table/tbody/tr[1]/td[1]/span[1]/a
/html/body/section/section/div[3]/div[1]/table/tbody/tr[1]/td[1]/span[1]/a

'''
b = webdriver.Firefox()
for j in range(545, 550):
    b.get("http://www.newsmth.net/nForum/#!board/MyPhoto?p=%s" % j)
    for i in range(1, 30, 1):
        print("-----第%s页第%s个   "%(j,i))
        time.sleep(4)
        eles = b.find_element_by_xpath('/html/body/section/section/div[3]/table/tbody/tr[%s]/td[2]/a' % i)
        eles.click()
        time.sleep(5)
        eles1 = b.find_elements_by_class_name("resizeable")
        author = b.find_element_by_class_name("a-u-name")
        print(author.text)

        k = 0
        print(len(eles1))
        try:

            for img in eles1:
                print("       ------")
                zz = img.get_attribute("src")
                urllib.request.urlretrieve(zz, "C:/tupia/%s_i%s_j%s_k%s.png" % (author.text, i + 1000, j, k))
                k = k + 1
                time.sleep(5)
        except:
            pass
        k = 0
        time.sleep(3)
        b.back()
