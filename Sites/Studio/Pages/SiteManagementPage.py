import time
import pyautogui
import sys
sys.path.append('C:/Users/skhalili/PycharmProjects/FirstSeleniumTest')
from Sites.Studio.Locators.locators import Locators
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
# to generate phone number
import random as r
# to read and write to files
import os
import csv


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
        # the first number should be in the range of 6 to 9
        self.ph_no.append(r.randint(6, 9))
        # the for loop is used to append the other 9 numbers.
        # the other 9 numbers can be in the range of 0 to 9.
        for i in range(1, 10):
            self.ph_no.append(r.randint(0, 9))

        strings = [str(integer) for integer in self.ph_no]
        phone_no_str = "".join(strings)
        # phone_no_int = int(phone_no_str)
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
