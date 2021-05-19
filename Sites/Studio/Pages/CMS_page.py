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


class CMSPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard = Locators.rmdy_studio_logo_xpath
        self.cmsbutton = Locators.cms_button_xpath
        self.add_folder_button = Locators.add_folder_button_id
        self.folder_name_field = Locators.folder_name_text_field_id
        self.add_button = Locators.add_button_xpath
        self.rowNumber=1
        self.add_document_xpath = Locators.add_document_button_xpath
        self.add_article_xpath = Locators.add_article_xpath
        self.article_title_xpath = Locators.article_title_xpath
        self.article_author_id = Locators.article_author_id
        self.article_body_xpath = Locators.article_body_xpath
        self.article_save_id = Locators.article_save_button
        self.go_back_to_cms_xpath = Locators.Go_back_to_CMS_xpath
        self.add_video_xpath = Locators.add_video_xpath
        self.add_video_title_id = Locators.add_video_title_id
        self.choose_file_xpath = Locators.add_video_choose_file_xpath
        self.add_video_file_name_id = Locators.add_video_file_name_id

    def showdashboard(self):

        self.driver.find_element_by_xpath(self.dashboard).click()

    def click_cms_button(self):
        self.driver.find_element_by_xpath(self.cmsbutton).click()

    def click_add_folder_button(self):
        self.driver.find_element_by_id(self.add_folder_button).click()

    def enter_folder_name(self, folder_name):

        self.driver.find_element_by_id(self.folder_name_field).clear()
        self.driver.find_element_by_id(self.folder_name_field).send_keys(folder_name)

    def click_add_button(self):
         self.driver.find_element_by_xpath(self.add_button).click()

    def verify_added_folder(self, folder_name):
        # element = self.driver.find_element_by_xpath("//div[contains(., folder_name)")
        try:
            element = self.driver.find_element_by_link_text(folder_name)
        except NoSuchElementException:
            print("No files found ..........................")
            return False
        return True

    def add_document(self, folder_name):
        time.sleep(5)
        created_folder = self.driver.find_element_by_link_text(folder_name)
        created_folder.click()
        self.driver.find_element_by_xpath(self.add_document_xpath).click()
        self.driver.find_element_by_xpath(self.add_article_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.article_title_xpath).send_keys("Auto article")
        self.driver.find_element_by_id(self.article_author_id).send_keys("safa")
        self.driver.switch_to.frame(self.driver.find_element_by_id("ifrmaejHtmlArea"))
        self.driver.find_element_by_xpath(self.article_body_xpath).send_keys("My Article...")
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id(self.article_save_id).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.go_back_to_cms_xpath).click()

    def verify_ready_to_go_content(self):
        self.driver.find_element_by_link_text('Ready-to-go Content').click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.go_back_to_cms_xpath).click()

    def find_element_row(self, folder_name):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))
            table = self.driver.find_element_by_xpath('//*[@id="JSAjaxListFolders"]/div[3]/table')
            trs = table.find_elements_by_tag_name('tr')
            row_count = 0
            matched_row_count = 0
            for tr in trs:
                tds = tr.find_elements_by_tag_name('td')
                print(tr.text)
                for i, td in enumerate(tds):
                    # This for loop will iterate single row value. Here i is index value
                    # print(i)
                    print(td.text)
                    if i == 0 and  td.text == folder_name:
                        print("Matched {}: {}".format(i, td.text))
                        matched_row_count = row_count
                        print("matched_row_count :", matched_row_count)
                row_count = row_count + 1
            # will print all the column name  #//*[@id="TableGrid"]/div[1]/table/tbody/tr[4]/td[1]/a[3]
            # tr[4] -row [td1]-column a[3]-button



        except:
            print("could not find the column details")
        # element = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(" + str(matched_row_count) + ")" + " " + ".Delete")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(" + matched_row_count + ")" + " " + ".btn-info").click()

    def add_video(self, folder_name):
        created_folder = self.driver.find_element_by_link_text(folder_name)
        created_folder.click()
        self.driver.find_element_by_xpath(self.add_document_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.add_video_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.add_video_title_id).send_keys("Auto Video")
        self.driver.find_element_by_id(self.add_video_file_name_id).click()
        time.sleep(2)
        pyautogui.write(r"C:\Users\skhalili\PycharmProjects\FirstSeleniumTest\Sites\Studio\Media\sample-mp4-file.mp4")
        pyautogui.press('enter')
        # self.driver.find_element_by_id(Locators.add_video_file_save_button_id).click()
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, Locators.add_video_file_save_button_id)))
        element.click();
        time.sleep(15)
        self.driver.find_element_by_xpath(self.go_back_to_cms_xpath).click()

    def add_pdf(self, folder_name):
        created_folder = self.driver.find_element_by_link_text(folder_name)
        created_folder.click()
        self.driver.find_element_by_xpath(self.add_document_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_pdf_file_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_id(Locators.add_pdf_file_title_id).send_keys("Auto pdf")
        self.driver.find_element_by_xpath(Locators.add_pdf_choose_file_xpath).click()
        time.sleep(2)
        pyautogui.write(r"C:\Users\skhalili\PycharmProjects\FirstSeleniumTest\Sites\Studio\Media\Sample_pdf.pdf")
        pyautogui.press('enter')
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_pdf_file_save_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.go_back_to_cms_xpath).click()

    def add_photo(self, folder_name):
        created_folder = self.driver.find_element_by_link_text(folder_name)
        created_folder.click()
        self.driver.find_element_by_xpath(self.add_document_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_photo_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_photo_name_xpath).send_keys("Auto photo :)")
        self.driver.find_element_by_xpath(Locators.add_photo_choose_file_button_xpath).click()
        time.sleep(2)
        pyautogui.write(r"C:\Users\skhalili\PycharmProjects\FirstSeleniumTest\Sites\Studio\Media\Moose.jpg")
        pyautogui.press('enter')
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_photo_save_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.go_back_to_cms_xpath).click()

    def add_survey(self, folder_name):

        created_folder = self.driver.find_element_by_link_text(folder_name)
        created_folder.click()
        self.driver.find_element_by_xpath(self.add_document_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_survey_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_survey_title_xpath).send_keys("Auto survey")
        self.driver.find_element_by_xpath(Locators.add_survey_author_xpath).send_keys("Auto author")
        self.driver.find_element_by_xpath(Locators.add_survey_link_url_xpath).send_keys("https://www.surveygizmo.com/s3/6306790/Template224-Testing")
        self.driver.find_element_by_xpath(Locators.add_survey_save_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.go_back_to_cms_xpath).click()

    def add_a_question(self, folder_name):
        created_folder = self.driver.find_element_by_link_text(folder_name)
        created_folder.click()
        self.driver.find_element_by_xpath(self.add_document_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_a_question_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_a_question_title_xpath).send_keys("Auto question")
        self.driver.find_element_by_xpath(Locators.add_a_question_xpath).send_keys("Auto author")
        self.driver.find_element_by_xpath(Locators.add_a_question_select_no_answers_xpath).click()
        self.driver.find_element_by_xpath(Locators.add_a_question_no_answers_3_xpath).click()
        self.driver.find_element_by_xpath(Locators.add_a_question_no_answers_3_xpath).click()
        self.driver.find_element_by_xpath(Locators.add_a_question_answer1).send_keys("Auto question1")
        self.driver.find_element_by_xpath(Locators.add_a_question_answer2).send_keys("Auto question2")
        self.driver.find_element_by_xpath(Locators.add_a_question_answer3).send_keys("Auto question3")
        self.driver.find_element_by_xpath(Locators.add_a_question_save_button_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.go_back_to_cms_xpath).click()

