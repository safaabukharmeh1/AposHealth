import time
from Sites.Studio.Locators.locators import Locators
import random as r


class PlanTemplate:
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver
        cls.dashboard = Locators.rmdy_studio_logo_xpath
        cls.random_no = []
        cls.password = "123456Qa"
        cls.location = "East Street"

    def generate_us_phone_number(self):
        # the first number should be in the range of 6 to 9
        self.random_no.append(r.randint(6, 9))
        # the for loop is used to append the other 9 numbers.
        # 9 numbers can be in the range of 0 to 9.
        for i in range(1, 10):
            self.random_no.append(r.randint(0, 9))
        strings = [str(integer) for integer in self.random_no]
        random_no_str = "".join(strings)
        return random_no_str

    def showdashboard(self):
        self.driver.find_element_by_xpath(Locators.rmdy_studio_logo_xpath).click()

    def plan_new_template(self):
        self.driver.find_element_by_xpath(Locators.plan_template_button_xpath).click()
        time.sleep(5)
        random_phone = self.generate_us_phone_number()
        new_template_name = "AuT" + random_phone
        self.driver.find_element_by_xpath(Locators.plan_template_create_new_template_button_xpath).click()
        self.driver.find_element_by_id(Locators.plan_template_template_name_id).send_keys(new_template_name)
        self.driver.find_element_by_xpath(Locators.plan_template_test_site_xpath).click()
        self.driver.find_element_by_id(Locators.plan_template_description_id).send_keys(new_template_name+" description !!!")
        self.driver.find_element_by_xpath(Locators.plan_template_save_button_xpath).click()
        self.driver.find_element_by_xpath(Locators.plan_template_next_first_tab_xpath).click()
