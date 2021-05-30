from Sites.Studio.Pages.cmspage import CMSPage
from Sites.Studio.Pages.PlanTemplatePage import PlanTemplate
from Sites.Studio.Core import StudioBaseClass
import pytest
import time


class TestPlanTemplate(StudioBaseClass.StudioBaseClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @pytest.mark.set1
    def test7_create_new_plan(self):
        plan = PlanTemplate(self.driver)
        cms = CMSPage(self.driver)
        self.login_site2()
        cms.show_dashboard()
        plan.showdashboard()
        plan.plan_new_template()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Test Completed")