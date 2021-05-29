import unittest
import sys
from selenium import webdriver
sys.path.append('/')
import configparser
from Sites.Studio.Pages.loginPage import LoginPage
from Sites.Studio.Pages.selecSite import SelectSite


class StudioBaseClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../../../Library/chromedriver.exe")
        cls.driver.set_page_load_timeout(30)
        cls.driver.maximize_window()
        # set implicit wait time
        cls.driver.implicitly_wait(20)  # second

    def login_site2(self):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        # print(config.sections())
        username = config.get('credentials', 'username')
        password = config.get('credentials', 'password')
        url = config.get('url', 'studio_stg_url')
        driver = self.driver
        select_site = SelectSite(self.driver)
        self.driver.get(url)
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        select_site.click_site2(self.driver)
