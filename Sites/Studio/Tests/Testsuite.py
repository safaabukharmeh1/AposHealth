# import pytest
from login import LoginTest
from CMS import TestCMS
from sitemanagement import TestSiteManagement
from Coachmanager import TestCoachManager
from sitemanagement import TestSiteManagement
from plantemplate import TestPlanTemplate
import unittest


def my_test_suite():
    # get all tests
    unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TestLoader().loadTestsFromTestCase(TestCMS)
    unittest.TestLoader().loadTestsFromTestCase(TestSiteManagement)
    unittest.TestLoader().loadTestsFromTestCase(TestCoachManager)
    unittest.TestLoader().loadTestsFromTestCase(TestSiteManagement)
    unittest.TestLoader().loadTestsFromTestCase(TestPlanTemplate)

