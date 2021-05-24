import sys
sys.path.append('C:/Users/skhalili/PycharmProjects/FirstSeleniumTest')
print(sys.path)

from selenium import webdriver
import time
import unittest
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Sites.Studio.Pages.loginPage import LoginPage
from Sites.Studio.Pages.homePage import HomePage
from Sites.Studio.Pages.selecSite import SelectSite

import HTMLTestRunner
import pytest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../../../Library/chromedriver.exe")
        cls.driver.set_page_load_timeout(15)
        cls.driver.maximize_window()

    @pytest.mark.set1
    def test_login_valid(self, username="skhalili_Admin", password="86HbDEy2"):
        driver = self.driver
        select_site = SelectSite(driver)
        self.driver.get("https://studio-stg.aposhealth.com/CoachConsole/Account/Login")
        login = LoginPage(driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
       # self.driver.find_element_by_name("UserName").send_keys("skhalili_Admin")
        #self.driver.find_element_by_name("Password").send_keys("86HbDEy2")
       # self.driver.find_element_by_xpath("/html/body/div/section/div[1]/div/div[2]/form/div[4]/button").click()
       # time.sleep(4)

        select_site.click_site2(driver)
        # homepage = HomePage(driver)
        # homepage.click_arrow(driver)
        # homepage.click_logout(driver)
    # Click Login
    def Login(self, username="skhalili_Admin", password="86HbDEy2"):
        driver = self.driver
        select_site = SelectSite(driver)
        self.driver.get("https://studio-stg.aposhealth.com/CoachConsole/Account/Login")
        login = LoginPage(driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        select_site.click_site2(driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main()


#time.sleep(4)
#driver.find_element_by_xpath("/html/body/div/section/div/div/div/div[2]/ul/li[2]/a/div/h2").click()
#driver.find_element_by_xpath("//*[@id='shrinkNav']/div[1]/div[1]/h1").click()
#driver.find_element_by_xpath("/html/body/div[1]/div[3]/section/div[2]/div[2]/div[1]/div/div[3]/div/a").click()
#driver.find_element_by_id("AddFolderBtn")