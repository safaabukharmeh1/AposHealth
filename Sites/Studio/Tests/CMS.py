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
from Sites.Studio.Pages.CMS_page import CMSPage


import unittest
import HTMLTestRunner
import pytest

class TestCMS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../../../Library/chromedriver.exe")
        cls.driver.set_page_load_timeout(20)
        cls.driver.maximize_window()
        cls.username = "skhalili_Admin"
        cls.password = "86HbDEy2"
        cls.folder_name = "auto_" + str(random.random())
        # cls.folder_name = "auto_0.7799667430933489"

    @pytest.mark.set1
    def test_1_create_cms_folder(self):
        driver = self.driver
        self.driver.get("https://studio-stg.aposhealth.com/CoachConsole/Account/Login")
        self.driver.set_page_load_timeout(15)
        login = LoginPage(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()
        self.driver.set_page_load_timeout(15)
        # self.driver.find_element_by_name("UserName").send_keys("skhalili_Admin")
        # self.driver.find_element_by_name("Password").send_keys("86HbDEy2")
        # self.driver.find_element_by_xpath("/html/body/div/section/div[1]/div/div[2]/form/div[4]/button").click()
        # time.sleep(4)
        select_site = SelectSite(driver)
        select_site.click_site2(driver)
        self.driver.set_page_load_timeout(15)
        cms = CMSPage(driver)
        time.sleep(2)
        cms.showdashboard()
        cms.click_cms_button()
        print(cms.verify_added_folder(self.folder_name))
        # if folder doesn't exist create it
        if not cms.verify_added_folder(self.folder_name):
            cms.click_add_folder_button()
            time.sleep(5)
            cms.enter_folder_name(self.folder_name)
            time.sleep(2)
            cms.click_add_button()
            time.sleep(5)

    @pytest.mark.set1
    def test_2_add_article(self):
        driver = self.driver
        self.driver.get("https://studio-stg.aposhealth.com/CoachConsole/Account/Login")
        self.driver.set_page_load_timeout(20)
        time.sleep(5)
        login = LoginPage(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()
        self.driver.set_page_load_timeout(15)
        # self.driver.find_element_by_name("UserName").send_keys("skhalili_Admin")
        # self.driver.find_element_by_name("Password").send_keys("86HbDEy2")
        # self.driver.find_element_by_xpath("/html/body/div/section/div[1]/div/div[2]/form/div[4]/button").click()
        # time.sleep(4)
        select_site = SelectSite(driver)
        select_site.click_site2(driver)
        self.driver.set_page_load_timeout(30)
        cms = CMSPage(driver)
        time.sleep(5)
        cms.showdashboard()
        cms.click_cms_button()
        # cms.verify_ready_to_go_content()
        # time.sleep(5)
        print(self.folder_name)
        if cms.verify_added_folder(self.folder_name):
            cms.add_document(self.folder_name)
            cms.add_pdf(self.folder_name)
            cms.add_photo(self.folder_name)
            cms.add_survey(self.folder_name)
            cms.add_a_question(self.folder_name)
            cms.add_video(self.folder_name)


    def dont_test3_find_element_row(self):
        driver = self.driver
        self.driver.get("https://studio-stg.aposhealth.com/CoachConsole/Account/Login")
        self.driver.set_page_load_timeout(20)
        login = LoginPage(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()
        self.driver.set_page_load_timeout(15)
        # self.driver.find_element_by_name("UserName").send_keys("skhalili_Admin")
        # self.driver.find_element_by_name("Password").send_keys("86HbDEy2")
        # self.driver.find_element_by_xpath("/html/body/div/section/div[1]/div/div[2]/form/div[4]/button").click()
        # time.sleep(4)
        select_site = SelectSite(driver)
        select_site.click_site2(driver)
        self.driver.set_page_load_timeout(30)
        cms = CMSPage(driver)
        cms.showdashboard()
        cms.click_cms_button()
        cms.find_element_row('RMDY Test Folder')




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main()
