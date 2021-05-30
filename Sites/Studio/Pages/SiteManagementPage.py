import time
from Sites.Studio.Locators.locators import Locators
import random as r


class SiteManagement:
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver
        cls.dashboard = Locators.rmdy_studio_logo_xpath
        cls.ph_no = []
        cls.password = "123456Qa"
        cls.patientsfile = "patientsfile"


    def open_test_site_management(self):
        self.driver.find_element_by_id(Locators.new_patient_select_test_site_id).click()

    def generate_us_phone_number(self):
        self.ph_no.append(r.randint(6, 9))
        for i in range(1, 10):
            self.ph_no.append(r.randint(0, 9))
        strings = [str(integer) for integer in self.ph_no]
        phone_no_str = "".join(strings)
        return phone_no_str

    def create_new_patient(self):
        self.driver.find_element_by_id(Locators.new_patient_button_id).click()
        time.sleep(2)
        self.ph_no = self.generate_us_phone_number()
        new_patient_name = "Au" + self.ph_no
        self.driver.find_element_by_id(Locators.new_patient_first_name_field_id).send_keys(new_patient_name)
        self.driver.find_element_by_id(Locators.new_patient_last_name_field_id).send_keys(new_patient_name)
        self.driver.find_element_by_id(Locators.new_patient_preferred_name_field_id).send_keys(new_patient_name)
        self.driver.find_element_by_id(Locators.new_patient_phone_number_field_id).send_keys(self.ph_no)
        self.driver.find_element_by_id(Locators.new_patient_user_name_field_id).send_keys(new_patient_name)
        self.driver.find_element_by_id(Locators.new_patient_password_field_id).send_keys(self.password)
        self.driver.find_element_by_id(Locators.new_patient_password_confirm_id).send_keys(self.password)
        self.driver.find_element_by_id(Locators.new_patient_preferred_language_id).click()
        self.driver.find_element_by_xpath(Locators.new_patient_preferred_english_xpath).click()
        self.driver.find_element_by_id(Locators.new_patient_email_field_id).send_keys(new_patient_name + "@mailinator.com")
        self.driver.find_element_by_id(Locators.new_patient_location_field_id).send_keys("East Street")
        self.driver.find_element_by_id(Locators.new_patient_birth_date_field_id).send_keys("05/18/1950")
        f = open("patient.txt", "w+")
        f.write(new_patient_name)
        f.close()
        self.driver.find_element_by_id(Locators.new_patient_save_button_id).click()
