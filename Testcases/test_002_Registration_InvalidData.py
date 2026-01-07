from Base.InitiateDriver import startBrowser,closeBrowser
def test_validateRegistration():
    driver = startBrowser()
    driver.find_element('xpath',"//input[@name = 'firstname']").send_keys('12345')
    driver.find_element('xpath',"//input[@name = 'lastname']").send_keys('!@#$%')
    driver.find_element('name','birthday_month').send_keys('Feb')
    driver.find_element('name','birthday_day').send_keys('28')
    driver.find_element('name','birthday_year').send_keys('2002')
    driver.find_element('xpath',"//input[@value='2']").click()
    driver.find_element('xpath',"//input[@aria-label='Mobile number or email']").send_keys('9898989898')
    driver.find_element('xpath',"//input[@aria-label='New password']").send_keys('Ram@1234')
    driver.find_element('xpath',"//button[@type='submit']").click()
    closeBrowser()
