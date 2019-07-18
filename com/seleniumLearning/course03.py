from selenium import webdriver

b = webdriver.Firefox()
b.get("http://www.maiziedu.com")
b.maximize_window()
z = b.find_element_by_link_text("Python全栈开发")
z.click()
b.back()

ele = b.find_element_by_css_selector('html body.YaHei.index div.main div.side-bar div.side-menu.w1920 div.w1920-scroll div.side-nav ul li.icon-3 a')
ele.click()
b.back()

ele = b.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[2]/ul/li[3]/a')
ele.click()
b.back()




