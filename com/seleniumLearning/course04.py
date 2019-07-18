#xpath定位
#https://blog.csdn.net/kaka1121/article/details/51811296

from selenium import webdriver
b = webdriver.Firefox()
b.get("http://www.cug.edu.cn/")
#使用 属性名 加路径组合方式
ele1 = b.find_elements_by_xpath('/html/body/div[3]/div/div/ul/li[2]/a[@target="_blank"]')
print(type(ele1))
print(len(ele1))
ele1[0].click()

b.back()
ele2 = b.find_elements_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/a[1][@href="js/xs.htm"]')
if len(ele2)>0:
    print('find second')
    ele2[0].click()
    b.back()


