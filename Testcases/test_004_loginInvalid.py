from Base.InitiateDriver import startBrowser,closeBrowser
def test_validateRegistration():
    driver = startBrowser()
    driver.find_element('xpath',"//input[@aria-label='Email or phone number']").send_keys('shyam')
    driver.find_element('xpath',"//input[@aria-label='Password']").send_keys('123456')
    driver.find_element('xpath',"//button[@type='submit']").click()
    closeBrowser()