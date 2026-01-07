from Base.InitiateDriver import startBrowser,closeBrowser
from Library.configReader import ElementsRead
def test_validateRegistration():
    driver = startBrowser()
    #driver.find_element('name','firstname').send_keys('Ram')
    driver.find_element('name',ElementsRead('Registration','fname')).send_keys('Ram')
    # driver.find_element('name','lastname').send_keys('yadhu')
    driver.find_element('name',ElementsRead('Registration','lname')).send_keys('yadhu')
    # driver.find_element('name','birthday_month').send_keys('Feb')
    # driver.find_element('name','birthday_day').send_keys('28')
    # driver.find_element('name','birthday_year').send_keys('2002')
    driver.find_element('name',ElementsRead('Registration','b_month')).send_keys('Feb')
    driver.find_element('name',ElementsRead('Registration','b_day')).send_keys('28')
    driver.find_element('name',ElementsRead('Registration','b_year')).send_keys('2002')

    # driver.find_element('xpath',"//input[@value='2']").click()
    driver.find_element('xpath',ElementsRead('Registration','gender_xpath')).click()

    # driver.find_element('xpath',"//input[@aria-label='Mobile number or email']").send_keys('9898989898')
    driver.find_element('xpath',ElementsRead('Registration','mobile_xpath')).send_keys('9898989898')

    # driver.find_element('xpath',"//input[@aria-label='New password']").send_keys('Ram@1234')
    driver.find_element('xpath',ElementsRead('Registration','password_xpath')).send_keys('Ram@1234')

    # driver.find_element('xpath',"//button[@type='submit']").click()
    driver.find_element('xpath',ElementsRead('Registration','submit_xpath')).click()
    closeBrowser()