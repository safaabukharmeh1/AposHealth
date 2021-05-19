# import pytest
from login import LoginTest
from CMS import TestCMS
from sitemanagement import TestSiteManagement
from Coachmanager import TestCoachManager
import unittest


def my_test_suite():
    # get all tests
    unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TestLoader().loadTestsFromTestCase(TestCMS)
    unittest.TestLoader().loadTestsFromTestCase(TestSiteManagement)
    unittest.TestLoader().loadTestsFromTestCase(TestCoachManager)

    # login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # cms = unittest.TestLoader().loadTestsFromTestCase(TestCMS)
    # create_patient = unittest.TestLoader().loadTestsFromTestCase(TestSiteManagement)
    # create_coach = unittest.TestLoader().loadTestsFromTestCase(TestCoachManager)
    # coach = unittest.TestLoader().loadTestsFromTestCase(TestCoachManager)
    # create a test suite combining Login and coach
    # login, cms, create_patient,
    # test_suite = unittest.TestSuite([create_coach])
    # unittest.TextTestRunner(verbosity=2).run(test_suite)
