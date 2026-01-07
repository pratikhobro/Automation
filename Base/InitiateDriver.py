from selenium.webdriver import Chrome,Firefox,Edge
from Library.configReader import configRead

def startBrowser():
    global driver
    if configRead('Details','browser')=='Chrome':
        driver=Chrome()
    elif configRead('Details','browser')=='Firefox':
        driver=Firefox()
    else:
        driver=Edge()
    #driver=Chrome()
    driver.get(configRead('Details','APP_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()