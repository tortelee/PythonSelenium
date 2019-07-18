from selenium import webdriver

brower = webdriver.Firefox()

brower.get("http://www.baidu.com")
print(brower.title)
if "百度" in brower.title:
    print(brower.current_url)
    z = brower.find_element_by_id("kw")
    print(type(z))  # webelement
    z.clear()
    z.send_keys("李涛涛")
    baidu = brower.find_element_by_id("su")
    baidu.submit()


def test_send_keys(url, id_name, context):
    b = webdriver.Firefox()
    b.get(url)

    ele = b.find_element_by_id(id_name)
    if ele is None:
        return 0
    ele.send_keys(context)
    ele2 = b.find_element_by_id("su")  # 提交按钮
    ele2.submit()
    return 0
