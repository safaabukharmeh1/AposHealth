import unittest
import sys
sys.path.append('C:/Users/skhalili/PycharmProjects/FirstSeleniumTest')
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time
import random

# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
sys.path.append('C:/Users/skhalili/PycharmProjects/FirstSeleniumTest')
print(sys.path)
from Sites.Studio.Pages.loginPage import LoginPage
from Sites.Studio.Pages.homePage import HomePage
from Sites.Studio.Pages.selecSite import SelectSite
from Sites.Studio.Pages.cmspage import CMSPage
from Sites.Studio.Pages.PlanTemplatePage import PlanTemplate

import unittest
import HTMLTestRunner


class TestPlanTemplate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../../../Library/chromedriver.exe")
        cls.driver.set_page_load_timeout(50)
        cls.driver.maximize_window()
        cls.username = "skhalili_Admin"
        cls.password = "86HbDEy2"
        # cls.folder_name = "auto_" + str(random.random())
        # # cls.folder_name = "auto_0.7799667430933489"

    def test_9_create_new_plan(self):
        driver = self.driver
        plan = PlanTemplate(driver)
        self.driver.get("https://studio-stg.aposhealth.com/CoachConsole/Account/Login")
        self.driver.set_page_load_timeout(30)
        login = LoginPage(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()
        self.driver.set_page_load_timeout(40)
        # self.driver.find_element_by_name("UserName").send_keys("skhalili_Admin")
        # self.driver.find_element_by_name("Password").send_keys("86HbDEy2")
        # self.driver.find_element_by_xpath("/html/body/div/section/div[1]/div/div[2]/form/div[4]/button").click()
        # time.sleep(4)
        select_site = SelectSite(driver)
        select_site.click_site2(driver)
        self.driver.set_page_load_timeout(15)
        plan.showdashboard()
        plan.plan_new_template()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")