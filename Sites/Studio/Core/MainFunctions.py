import sys
from selenium import webdriver
sys.path.append('/')
print(sys.path)


import HTMLTestRunner
import pytest
import configparser


class MainFunction:
    @classmethod
    def setupclass(cls):
        cls.driver = webdriver.Chrome("../../../Library/chromedriver.exe")
        cls.driver.set_page_load_timeout(15)
        cls.driver.maximize_window()

    def login_site2(self):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        print(config.sections())
        username = config.get('credentials', 'username')
        password = config.get('credentials', 'password')
        url = config.get('url', 'studio_stg_url')
        driver = self.driver
        select_site = SelectSite(driver)
        self.driver.get(url)
        login = LoginPage(driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        select_site.click_site2(driver)
        return driver

    def get_config(self, section, key):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        print(config.sections())
        value = config.get(section, key)
        return value

