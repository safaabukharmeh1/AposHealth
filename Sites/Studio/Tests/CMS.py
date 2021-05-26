import sys
sys.path.append('C:/Users/skhalili/PycharmProjects/FirstSeleniumTest')
import time
import random
from Sites.Studio.Core import MainFunctions, StudioBaseClass

sys.path.append('C:/Users/skhalili/PycharmProjects/FirstSeleniumTest')
print(sys.path)
from Sites.Studio.Pages.cmspage import CMSPage
import pytest


class TestCMS(StudioBaseClass.StudioBaseClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # cls.driver = webdriver.Chrome("../../../Library/chromedriver.exe")
        # cls.driver.set_page_load_timeout(20)
        # cls.driver.maximize_window()
        cls.folder_name = "auto_" + str(random.random())
        # cls.folder_name = "auto_0.7799667430933489"

    @pytest.mark.set1
    def test_1_create_cms_folder(self):

        self.login_site2()
        time.sleep(3)
        # driver = MainFunctions.MainFunction.login_site2(self)
        cms = CMSPage(self.driver)
        time.sleep(2)
        cms.show_dashboard()
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
        cms = CMSPage(self.driver)
        video_url = MainFunctions.MainFunction.get_config(self, "url", "Video")
        photo_url = MainFunctions.MainFunction.get_config(self, "url", "photo")
        pdf_url = MainFunctions.MainFunction.get_config(self, "url", "pdf")
        print(self.folder_name)
        if cms.verify_added_folder(self.folder_name):
            cms.add_document(self.folder_name)
            cms.add_pdf(self.folder_name, pdf_url)
            time.sleep(3)
            cms.add_photo(self.folder_name, photo_url)
            time.sleep(3)
            cms.add_survey(self.folder_name)
            time.sleep(3)
            cms.add_a_question(self.folder_name)
            time.sleep(3)
            cms.add_video(self.folder_name, video_url)

    def find_element_row(self):
        driver = MainFunctions.MainFunction.login_site2(self)
        cms = CMSPage(driver)

        # was used to login
        # used login from main function instead
        # driver = self.driver
        # self.driver.get("https://studio-stg.aposhealth.com/CoachConsole/Account/Login")
        # self.driver.set_page_load_timeout(20)
        # login1 = LoginPage(driver)
        # login1.enter_username(self.username)
        # login1.enter_password(self.password)
        # login1.click_login()
        # self.driver.set_page_load_timeout(15)
        # select_site = SelectSite(driver)
        # select_site.click_site2(driver)
        self.driver.set_page_load_timeout(30)
        cms.show_dashboard()
        cms.click_cms_button()
        cms.find_element_row('RMDY Test Folder')

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Test Completed")


