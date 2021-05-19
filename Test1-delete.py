from selenium import webdriver
import time

driver = webdriver.Chrome('Library/chromedriver.exe')

driver.set_page_load_timeout(20)
driver.maximize_window()
driver.get("https://studio-stg.aposhealth.com/CoachConsole")
driver.find_element_by_name("UserName").send_keys("skhalili_Admin")
driver.find_element_by_name("Password").send_keys("86HbDEy2")

driver.find_element_by_xpath("/html/body/div/section/div[1]/div/div[2]/form/div[4]/button").click()

time.sleep(4)
driver.find_element_by_xpath("/html/body/div/section/div/div/div/div[2]/ul/li[2]/a/div/h2").click()
driver.find_element_by_xpath("//*[@id='shrinkNav']/div[1]/div[1]/h1").click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/section/div[2]/div[2]/div[1]/div/div[3]/div/a").click()
driver.find_element_by_id("AddFolderBtn")






