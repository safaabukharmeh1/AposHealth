import sys
import time
import random
import pytest
from Sites.Studio.Locators.locators import Locators
from Sites.Studio.Pages.cmspage import CMSPage
from Sites.Studio.Core import MainFunctions, StudioBaseClass
from selenium.common.exceptions import NoSuchElementException


class TestCMS(StudioBaseClass.StudioBaseClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.folder_name = "auto_" + str(random.random())
        cls.video_url = MainFunctions.MainFunction.get_config(cls, "url", "Video")
        cls.photo_url = MainFunctions.MainFunction.get_config(cls, "url", "photo")
        cls.pdf_url = MainFunctions.MainFunction.get_config(cls, "url", "pdf")
        cls.cms = CMSPage(cls.driver)

    @pytest.mark.set1
    def test1_create_cms_folder(self):
        self.login_site2()
        time.sleep(3)
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
            f = open("cms_folder.txt", "w+")
            f.write(self.folder_name)
            f.close()
        else:
            print("Oops! folder " + self.folder_name + " exist !!!")
            raise

    @pytest.mark.set1
    def test2_add_article(self):
        cms = CMSPage(self.driver)
        print(self.folder_name)
        if cms.verify_added_folder(self.folder_name):
            cms.add_document(self.folder_name)
            cms.add_pdf(self.folder_name, self.pdf_url)
            time.sleep(3)
            cms.add_photo(self.folder_name, self.photo_url)
            time.sleep(3)
            cms.add_survey(self.folder_name)
            time.sleep(3)
            cms.add_a_question(self.folder_name)
            time.sleep(3)
            cms.add_video(self.folder_name, self.video_url)
        else:
            raise Exception("Sorry folder is not available !")

    def test4_delete_folder(self):
        self.login_site2()
        time.sleep(3)
        cms = CMSPage(self.driver)
        time.sleep(2)
        cms.show_dashboard()
        cms.click_cms_button()

        row = cms.find_element_row() - 1
        delete_folder_xpath = "//tbody/tr[" + str(row) + "]/td[3]/span[3]"
        delete_folder = self.driver.find_element_by_xpath(delete_folder_xpath)
        delete_folder.click()
        time.sleep(2)
        yes_button = self.driver.find_element_by_xpath(Locators.yes_button_xpath)
        yes_button.click()

        # assert delete
        time.sleep(5)
        self.driver.refresh()
        # get folder name
        f = open("cms_folder.txt", "r")
        folder_name = f.read()
        f.close()
        try:
            self.driver.find_element_by_link_text(folder_name)
            raise ValueError("folder: " + folder_name + " Still exist!")
        except NoSuchElementException:
            print ("Folder: " + folder_name + " was deleted successfully!")

    def test3_delete_folder_content(self):
        self.login_site2()
        time.sleep(20)
        self.cms.show_dashboard()
        time.sleep(10)
        self.cms.click_cms_button()
        self.cms.delete_folder_content()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")



