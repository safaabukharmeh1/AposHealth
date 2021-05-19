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


class CoachManager:
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver
        cls.dashboard = Locators.rmdy_studio_logo_xpath
        cls.random_no = []
        cls.password = "123456Qa"
        cls.location = "East Street"
        cls.new_coach_name = ""

    def generate_us_phone_number(self):
        # the first number should be in the range of 6 to 9
        self.random_no.append(r.randint(6, 9))
        # the for loop is used to append the other 9 numbers.
        # the other 9 numbers can be in the range of 0 to 9.
        for i in range(1, 10):
            self.random_no.append(r.randint(0, 9))

        strings = [str(integer) for integer in self.random_no]
        random_no_str = "".join(strings)
        # phone_no_int = int(phone_no_str)
        return random_no_str

    def showdashboard(self):
        self.driver.find_element_by_xpath(Locators.rmdy_studio_logo_xpath).click()

    def create_new_coach(self):
        self.driver.find_element_by_xpath(Locators.coach_manager_button_xpath).click()
        time.sleep(5)
        random_phone = self.generate_us_phone_number()
        self.new_coach_name = "AuC" + random_phone
        self.driver.find_element_by_id(Locators.coach_manager_new_coach_button_id).click()
        self.driver.find_element_by_id(Locators.coach_manager_first_name_field_id).send_keys(self.new_coach_name)
        self.driver.find_element_by_id(Locators.coach_manager_last_name_field_id).send_keys(self.new_coach_name)
        self.driver.find_element_by_id(Locators.coach_manager_title_field_id).send_keys("Mr")
        self.driver.find_element_by_id(Locators.coach_manager_user_name_id).send_keys(self.new_coach_name)
        self.driver.find_element_by_id(Locators.coach_manager_password_id).send_keys(self.password)
        self.driver.find_element_by_id(Locators.coach_manager_password_confirm_id).send_keys(self.password)
        self.driver.find_element_by_id(Locators.coach_manager_location_field_id).send_keys(self.location)
        self.driver.find_element_by_id(Locators.coach_manager_birthdate_field_id).send_keys("05/18/1950")
        self.driver.find_element_by_id(Locators.coach_manager_gender_list_id).click()
        self.driver.find_element_by_xpath(Locators.coach_manager_gender_male_xpath).click()
        self.driver.find_element_by_id(Locators.coach_manager_email_field_id).send_keys(self.new_coach_name+"@mailinator.com")
        self.driver.find_element_by_xpath(Locators.coach_manager_test_site_xpath).click()
        self.driver.find_element_by_id(Locators.coach_manager_about_me_field_id).send_keys("About me")
        self.driver.find_element_by_id(Locators.coach_manager_external_id_field_id).send_keys(random_phone)
        f = open("coach.txt", "w+")
        f.write(self.new_coach_name)
        f.close()
        self.driver.find_element_by_id(Locators.coach_manager_save_button_id).click()

    def find_coach(self):
        new_coach_name = self.new_coach_name
        self.driver.find_element_by_id(Locators.coach_manager_coach_user_name_id).send_keys(new_coach_name)
        self.driver.find_element_by_id(Locators.coach_manager_search_coach_button_id).click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))
        table = self.driver.find_element_by_xpath('//*[@id="pagedListContainer0"]/table')
        trs = table.find_elements_by_tag_name('tr')
        row_count = 0
        matched_row_count = 0
        try:
            for tr in trs:
                tds = tr.find_elements_by_tag_name('td')
                for i, td in enumerate(tds):
                    # This for loop will iterate single row value. Here i is index value
                    # print(i)
                    if i == 3 and td.text == new_coach_name:
                        # print("Matched {}: {}".format(i, td.text))
                        # matched_row_count = row_count
                        # print("matched_row_count :", matched_row_count)
                        print("Coach " + new_coach_name + " was added Successfully!, at row no: " + str(matched_row_count))
                row_count = row_count + 1

        except ValueError:
            print("could not find the coach")