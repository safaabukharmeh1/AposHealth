from Sites.Studio.Pages.SiteManagementPage import SiteManagement
from Sites.Studio.Core import MainFunctions, StudioBaseClass
import pytest
import time


class TestSiteManagement(StudioBaseClass.StudioBaseClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @pytest.mark.set1
    def test6_create_new_patient(self):
        self.login_site2()
        time.sleep(3)
        site = SiteManagement(self.driver)
        site.create_new_patient()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Test Completed")

