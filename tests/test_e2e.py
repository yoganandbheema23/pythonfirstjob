import time

from selenium.webdriver.common.by import By

from Utilities.Baseclass import BaseClass
from pageObjects.RegPage import Regpage


class TestOne(BaseClass):
    def test_e2e(self):
        print("End to end testing started...")
        regpage=Regpage(self.driver)
        #MyAccount xpath
        myAccountEle=self.driver.find_element(By.XPATH,"//div[@id='top-links']/ul/li[2]/a")
        myAccountEle.click()

        time.sleep(5)
        #Register link xpath
        registerButton=self.driver.find_element(By.XPATH,"//a[contains(text(),'Register')]")
        registerButton.click()

        #Registration form xpaths
        #first_name=self.driver.find_element(By.XPATH,"//input[@id='input-firstname']")
        regpage.provide_firstname_data().send_keys("TestFirstname")
        #first_name.send_keys("testName")

        regpage.provide_lastname_data().send_keys("TestLastname")

        regpage.provide_email_info().send_keys("yoga@gmail.com")

        regpage.provide_mobile_number_data().send_keys("8801636401")

        regpage.provide_password_info_data().send_keys("Test123&")

        regpage.provide_confPass_info_data().send_keys("Test123&")

        regpage.provide_radio_yes_data().click()

        regpage.click_privacy_chk().click()

        regpage.press_submit_btn().click()


