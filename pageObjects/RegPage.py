#import sheet as sheet
from selenium.webdriver.common.by import By


class Regpage:

    def __init__(self,driver):
        self.driver=driver

    first_name=(By.XPATH,"//input[@id='input-firstname']")
    last_name=(By.XPATH,"//input[@id='input-lastname']")
    email_info=(By.XPATH,"//input[@id='input-email']")
    mobile_number=(By.XPATH,"//input[@id='input-telephone']")
    password_info=(By.XPATH,"//input[@id='input-password']")
    confPass_info=(By.XPATH,"//input[@id='input-confirm']")
    radio_yes=(By.XPATH,"//input[@name='newsletter' and @value='1']")
    submit_btn=(By.XPATH,"//input[@value='Continue']")
    privacy_policy_chk=(By.XPATH,"//input[@type='checkbox']")

    def provide_firstname_data(self):
        return self.driver.find_element(*Regpage.first_name)

    def provide_lastname_data(self):
        return self.driver.find_element(*Regpage.last_name)

    def provide_email_info(self):
        return self.driver.find_element(*Regpage.email_info)

    def provide_mobile_number_data(self):
        return self.driver.find_element(*Regpage.mobile_number)

    def provide_password_info_data(self):
        return self.driver.find_element(*Regpage.password_info)

    def provide_confPass_info_data(self):
        return self.driver.find_element(*Regpage.confPass_info)

    def provide_radio_yes_data(self):
        return self.driver.find_element(*Regpage.radio_yes)

    def click_privacy_chk(self):
        return self.driver.find_element(*Regpage.privacy_policy_chk)
    def press_submit_btn(self):
        return self.driver.find_element(*Regpage.submit_btn)




