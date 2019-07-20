A HTTP cookie is comprised of information about the user and their preferences.
It stores information using a key-value pair.
It is a small piece of data sent from Web Application and stored in Web Browser,while the user is browsing that website.
we will learn:
- Selenium Query Commands for cookies 
- Why Handle Cookies in Selenium? 
- Demo: Cookie handling in Selenium. 
- Step 1) Storing cookie information. 
- Step 2) Using stored cookie to login into the application. 
#### Selenium Query Commands for cookies
In Selenium Webdriver, we can query and interact with cookies with below built-in method:
```python
driver.get_cookies()
```
#### Why Handle Cookies in Selenium?
Each cookie is associated with a name, value, domain, path, expiry, and the status of whether it is secure or not. In order to validate a client, a server parses all of these values in a cookie. 
When Testing a web application using selenium web driver, you may need to create, update or delete a cookie. 
For example, when automating Online Shopping Application, you many need to automate test scenarios like place order, View Cart, Payment Information, order confirmation, etc. 
If cookies are not stored, you will need to perform login action every time before you execute above listed test scenarios. This will increase your coding effort and execution time. 
The solution is to store cookies in a File. Later, retrieve the values of cookie from this file and add to it your current browser session. As a result, you can skip the login steps in every Test Case because your driver session has this information in it. 
The application server now treats your browser session as authenticated and directly takes you to your requested URL.
#### Demo: Cookie handling in Selenium.
We will use <https://stackoverflow.com/questions/15058462/how-to-save-and-load-cookies-using-python-selenium-webdriver> for our demo purpose. 
This will be a 2 step process. 
- Login into application and store the authentication cookie generated. 
-  Used the stored cookie, to again login into application without using userid and password. 
```$python

import selenium.webdriver 

driver = selenium.webdriver.Firefox()
driver.get("http://www.google.com")
driver.get_cookies()
for cookie in cookies:
    driver.add_cookie(cookie)
```
