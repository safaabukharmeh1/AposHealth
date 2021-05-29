import time
from Sites.Studio.Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

class CMSPage:
    def __init__(self, driver):
        self.driver = driver
        self.rowNumber = 1

    def show_dashboard(self):
        dashboard = self.driver.find_element_by_xpath(Locators.rmdy_studio_logo_xpath)
        dashboard.click()

    def click_cms_button(self):
        cms_button = self.driver.find_element_by_xpath(Locators.cms_button_xpath)
        cms_button.click()

    def click_add_folder_button(self):
        add_folder_button = self.driver.find_element_by_id(Locators.add_folder_button_id)
        add_folder_button.click()

    def enter_folder_name(self, folder_name):
        folder_name_text_field = self.driver.find_element_by_id(Locators.folder_name_text_field_id)
        folder_name_text_field.clear()
        folder_name_text_field.send_keys(folder_name)

    def click_add_button(self):
        add_button = self.driver.find_element_by_xpath(Locators.add_button_xpath)
        add_button.click()

    def click_go_back_to_folders(self):
        back_button = self.driver.find_element_by_xpath(Locators.go_back_to_folders)
        back_button.click()

    def verify_added_folder(self, folder_name):
        try:
            self.driver.find_element_by_link_text(folder_name)
        except NoSuchElementException:
            print("No files found ..........................")
            return False
        return True

    def add_document(self, folder_name):
        time.sleep(5)
        created_folder = self.driver.find_element_by_link_text(folder_name)
        created_folder.click()
        add_document_button = self.driver.find_element_by_xpath(Locators.add_document_button_xpath)
        add_document_button.click()
        add_article = self.driver.find_element_by_xpath(Locators.add_article_xpath)
        add_article.click()
        time.sleep(2)
        article_title = self.driver.find_element_by_xpath(Locators.article_title_xpath)
        article_title.send_keys("Auto article")
        article_author = self.driver.find_element_by_id(Locators.article_author_id)
        article_author.send_keys("Safa")
        # switch to new frame
        self.driver.switch_to.frame(self.driver.find_element_by_id("ifrmaejHtmlArea"))
        article_body = self.driver.find_element_by_xpath(Locators.article_body_xpath)
        article_body.send_keys("My Article...")
        # Switch back from frame
        self.driver.switch_to.default_content()
        article_save_button = self.driver.find_element_by_id(Locators.article_save_button)
        article_save_button.click()
        time.sleep(2)
        go_back_to_cms = self.driver.find_element_by_xpath(Locators.Go_back_to_CMS_xpath)
        go_back_to_cms.click()

    def verify_ready_to_go_content(self):
        ready_to_go = self.driver.find_element_by_link_text('Ready-to-go Content')
        ready_to_go.click()
        time.sleep(5)
        go_back_to_cms = self.driver.find_element_by_xpath(Locators.Go_back_to_CMS_xpath)
        go_back_to_cms.click()

    # find_element_row, used in finding folder row to delete that folder (cms.delete_folder)
    def find_element_row(self):
        try:
            f = open("cms_folder.txt", "r")
            folder_name = f.read()
            f.close()
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))
            table = self.driver.find_element_by_xpath('//*[@id="JSAjaxListFolders"]/div[3]/table')
            trs = table.find_elements_by_tag_name('tr')
            row_count = 0
            matched_row_count = 0
            for tr in trs:
                tds = tr.find_elements_by_tag_name('td')
                # print(tr.text)
                for i, td in enumerate(tds):
                    # This for loop will iterate single row value. Here i is index value
                    if i == 0 and td.text == folder_name:
                        # print("Matched {}: {}".format(i, td.text))
                        matched_row_count = row_count
                        # print("matched_row_count :", matched_row_count)
                row_count = row_count + 1
            # will print all the column name  #//*[@id="TableGrid"]/div[1]/table/tbody/tr[4]/td[1]/a[3]
            # tr[4] -row [td1]-column a[3]-button
            return row_count
        except NoSuchElementException:
            print("Could not find the column details")

    def add_video(self, folder_name, url):
        created_folder = self.driver.find_element_by_link_text(folder_name)
        created_folder.click()
        add_document = self.driver.find_element_by_xpath(Locators.add_document_button_xpath)
        add_document.click()
        time.sleep(2)
        add_video = self.driver.find_element_by_xpath(Locators.add_video_xpath)
        add_video.click()
        time.sleep(2)
        video_title = self.driver.find_element_by_id(Locators.add_video_title_id)
        video_title.send_keys("Auto Video")
        add_video_file_name = self.driver.find_element_by_id(Locators.add_video_file_name_id)
        add_video_file_name.click()
        time.sleep(2)
        pyautogui.write(url)
        pyautogui.press('enter')
        # self.driver.find_element_by_id(Locators.add_video_file_save_button_id).click()
        save_button = Locators.add_video_file_save_button_id
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, save_button)))
        element.click()
        time.sleep(20)
        go_back_to_cms = self.driver.find_element_by_xpath(Locators.Go_back_to_CMS_xpath)
        go_back_to_cms.click()

    def add_pdf(self, folder_name, pdf_url):
        created_folder = self.driver.find_element_by_link_text(folder_name)
        created_folder.click()
        self.driver.find_element_by_xpath(Locators.add_document_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_pdf_file_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_id(Locators.add_pdf_file_title_id).send_keys("Auto pdf")
        self.driver.find_element_by_xpath(Locators.add_pdf_choose_file_xpath).click()
        time.sleep(2)
        pyautogui.write(pdf_url)
        pyautogui.press('enter')
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_pdf_file_save_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.Go_back_to_CMS_xpath).click()

    def add_photo(self, folder_name, photo_url):
        created_folder = self.driver.find_element_by_link_text(folder_name)
        created_folder.click()
        self.driver.find_element_by_xpath(Locators.add_document_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_photo_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_photo_name_xpath).send_keys("Auto photo :)")
        self.driver.find_element_by_xpath(Locators.add_photo_choose_file_button_xpath).click()
        time.sleep(2)
        pyautogui.write(photo_url)
        pyautogui.press('enter')
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_photo_save_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.Go_back_to_CMS_xpath).click()

    def add_survey(self, folder_name):
        created_folder = self.driver.find_element_by_link_text(folder_name)
        created_folder.click()
        self.driver.find_element_by_xpath(Locators.add_document_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_survey_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.add_survey_title_xpath).send_keys("Auto survey")
        self.driver.find_element_by_xpath(Locators.add_survey_author_xpath).send_keys("Auto author")
        self.driver.find_element_by_xpath(Locators.add_survey_link_url_xpath).send_keys("https://www.surveygizmo.com/s3/6306790/Template224-Testing")
        self.driver.find_element_by_xpath(Locators.add_survey_save_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.Go_back_to_CMS_xpath).click()

    def add_a_question(self, folder_name):
        created_folder = self.driver.find_element_by_link_text(folder_name)
        created_folder.click()
        self.driver.find_element_by_xpath(Locators.add_document_button_xpath).click()
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
        self.driver.find_element_by_xpath(Locators.Go_back_to_CMS_xpath).click()

    def delete_folder_content(self):
        i = 1
        f = open("cms_folder.txt", "r")
        folder_name = f.read()
        f.close()
        folder = self.driver.find_element_by_link_text(folder_name)
        folder.click()
        while i < 7:
            delete_xpath = Locators.delete_article_xpath
            self.driver.find_element_by_xpath(delete_xpath).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(Locators.yes_button_xpath).click()
            time.sleep(5)
            i += 1
        self.driver.find_element_by_xpath(Locators.Go_back_to_CMS_xpath).click()



