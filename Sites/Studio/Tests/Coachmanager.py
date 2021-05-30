from selenium import webdriver
import time
from Sites.Studio.Pages.cmspage import CMSPage
from Sites.Studio.Pages.CoachManagerPage import CoachManager
from Sites.Studio.Core import StudioBaseClass
import pytest


class TestCoachManager(StudioBaseClass.StudioBaseClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @pytest.mark.set1
    def test5_create_new_coach(self):
        coach = CoachManager(self.driver)
        cms = CMSPage(self.driver)
        self.login_site2()
        cms.show_dashboard()
        coach.create_new_coach()
        coach.find_coach()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")