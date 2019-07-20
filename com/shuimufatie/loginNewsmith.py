from selenium import webdriver
from selenium.webdriver import ActionChains

'''
登录模块，和维护session的不一样，尽量分开吧
'''


class LoginMy:

    def loginNewSmith(url, usrName, password):
        b = webdriver.Firefox()
        b.get(url)

        eleUsr = b.find_element_by_id("id")
        elePw = b.find_element_by_id("pwd")
        eleClick = b.find_element_by_id("b_login")

        action = ActionChains(b)
        action.click(eleUsr)
        action.send_keys(usrName)
        action.click(elePw)
        action.send_keys(password)
        action.click(eleClick)
        action.perform()
        return b
