from Base.InitiateDriver import startBrowser,closeBrowser
def test_validateRegistration():
    driver = startBrowser()
    driver.find_element('xpath',"//input[@aria-label='Email or phone number']").send_keys('9987689981')
    driver.find_element('xpath',"//input[@aria-label='Password']").send_keys('Ram@12345')
    driver.find_element('xpath',"//button[@type='submit']").click()
    closeBrowser()