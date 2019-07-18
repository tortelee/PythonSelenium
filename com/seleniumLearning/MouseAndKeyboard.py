from selenium import webdriver
from selenium.webdriver import ActionChains

'''
鼠标悬停，获得submenu
'''
baidu = "https://www.baidu.com/"


def test_mouser_move(url, menu_id):
    b = webdriver.Firefox()
    b.get(url)
    # find the element
    menu = b.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[2]/a[@target="_blank"]')

    # create Action 初始化时传入驱动器
    action = ActionChains(b)
    action.move_to_element(menu)
    action.perform()
    b.close()
    return 0


test_mouser_move("http://www.cug.edu.cn/", "ww")
'''
拖拽，指的是鼠标先点击左键，然后移动，然后松开
'''


def test_mouser_drag(url, source, target):
    b = webdriver.Firefox()
    b.get(url)
    source1 = b.find_element_by_id(source)
    target1 = b.find_element_by_id(target)

    # create Action 初始化时传入驱动器
    action = ActionChains(b)
    action.drag_and_drop(source1, target1)
    action.perform()
    b.close()
    return 0


test_mouser_drag("https://www.baidu.com/", "lg", "kw")
'''
点击鼠标
'''


def test_mouse_click(url, id_name):
    b = webdriver.Firefox()
    b.get(url)
    # 找到元素
    buttom = b.find_element_by_id(id_name)
    # 创建action行为
    action = ActionChains(b)
    action.click(buttom)
    action.perform()
    b.close()
    return 0


test_mouse_click("https://www.baidu.com/", "su")
'''
百度输入搜索
acion会将操作放到self._actions（类型为list）队列中，
并返回self实例本身，然后通过perform方法，依次执行队列中的操作。
action可以触发事件，
'''


def test_send_keys(url, context):
    b = webdriver.Firefox()
    b.get(url)

    ins = b.find_element_by_id("kw")  #不需要往输入框输入数据，应该关联了，事件关联！！
    ins.send_keys(context)

    submit = b.find_element_by_id("su")
    action = ActionChains(b)
    action.click(ins)
    action.send_keys(context)
    action.click(submit)
    action.perform()
    b.close()
    return 0


test_send_keys(baidu, "你好啊")
