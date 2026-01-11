from Library.configReader import ElementsRead

class RegistrationData:
    def __init__(self,obj):
        global driver
        driver = obj
        
    def enterFirstName(self,firstname):
        driver.find_element('name',ElementsRead('Registration','fname')).send_keys(firstname)
        
    def enterLastName(self,lastname):
        driver.find_element('name',ElementsRead('Registration','lname')).send_keys(lastname)
        
    def enterBdMonth(self,bd_mon):
        driver.find_element('name',ElementsRead('Registration','b_month')).send_keys(bd_mon)
    
    def enterBdDate(self,bd_date):
        driver.find_element('name',ElementsRead('Registration','b_day')).send_keys(bd_date)
        
    def enterBdYear(self,bd_year):
        driver.find_element('name',ElementsRead('Registration','b_year')).send_keys(bd_year)
     
    def clickGender(self,genderData): 
        if genderData == 'Male':
            driver.find_element('xpath',ElementsRead('Registration','b')).click()
        elif genderData == 'Female':
            driver.find_element('xpath',ElementsRead('Registration','a')).click()
        else:
            driver.find_element('xpath',ElementsRead('Registration','c')).click()
        
    def enterMobile(self,mobile):
        driver.find_element('xpath',ElementsRead('Registration','mobile_xpath')).send_keys(mobile)
        
    def enterPassword(self,password):
        driver.find_element('xpath',ElementsRead('Registration','password_xpath')).send_keys(password)
        
    def clickSubmit(self):
        driver.find_element('xpath',ElementsRead('Registration','submit_xpath')).click()