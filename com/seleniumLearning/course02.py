from selenium import webdriver

brower = webdriver.Firefox()

brower.get("http://www.baidu.com")
print(brower.title)
if "百度" in brower.title:
    print(brower.current_url)
    z  = brower.find_element_by_id("kw")
    print(type(z))  #webelement
    z.clear()
    z.send_keys("李涛涛")
    baidu = brower.find_element_by_id("su")
    baidu.submit()
