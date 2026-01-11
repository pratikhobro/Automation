from Base.InitiateDriver import startBrowser,closeBrowser
from Library.configReader import ElementsRead
from Pages.RegistrationPage import RegistrationData
import pytest

def dataGenerator():
    listData = [
                ['Ram','Sharma','Feb','28','2002','9898989898','Ram@1234','Male'],
                ['Shyam','Giri','Dec','03','2004','9876000000','Shyam@123','Male'],
                ['Sita','Pandey','Jan','06','2003','9800000000','Sita@123','Female']
                ]
    return listData

@pytest.mark.parametrize('data',dataGenerator())
def test_validateRegistration(data):
    driver = startBrowser()
    #driver.find_element('name','firstname').send_keys('Ram')
    # driver.find_element('name',ElementsRead('Registration','fname')).send_keys('Ram')
    # # driver.find_element('name','lastname').send_keys('yadhu')
    # driver.find_element('name',ElementsRead('Registration','lname')).send_keys('yadhu')
    register = RegistrationData(driver)
    register.enterFirstName(data[0])
    register.enterLastName(data[1])
    # driver.find_element('name','birthday_month').send_keys('Feb')
    # driver.find_element('name','birthday_day').send_keys('28')
    # driver.find_element('name','birthday_year').send_keys('2002')
    # driver.find_element('name',ElementsRead('Registration','b_month')).send_keys('Feb')
    # driver.find_element('name',ElementsRead('Registration','b_day')).send_keys('28')
    # driver.find_element('name',ElementsRead('Registration','b_year')).send_keys('2002')
    register.enterBdMonth(data[2])
    register.enterBdDate(data[3])
    register.enterBdYear(data[4])

    # driver.find_element('xpath',"//input[@value='2']").click()
    # driver.find_element('xpath',ElementsRead('Registration','gender_xpath')).click()
    register.clickGender(data[7])

    # driver.find_element('xpath',"//input[@aria-label='Mobile number or email']").send_keys('9898989898')
    # driver.find_element('xpath',ElementsRead('Registration','mobile_xpath')).send_keys('9898989898')
    register.enterMobile(data[5])
    
    # driver.find_element('xpath',"//input[@aria-label='New password']").send_keys('Ram@1234')
    # driver.find_element('xpath',ElementsRead('Registration','password_xpath')).send_keys('Ram@1234')
    register.enterPassword(data[6])
    
    # driver.find_element('xpath',"//button[@type='submit']").click()
    # driver.find_element('xpath',ElementsRead('Registration','submit_xpath')).click()
    register.clickSubmit()
    
    closeBrowser()