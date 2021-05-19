from Sites.Studio.Locators.locators import Locators
class SelectSite:


    def __init__(self, driver):
        self.driver = driver
        self.site1_xpath = Locators.site1_xpath
        self.site2_xpath = Locators.site2_xpath

    def click_site1(self,driver):
        self.driver.find_element_by_xpath(self.site1_xpath).click()

    def click_site2(self,driver):
        self.driver.find_element_by_xpath(self.site2_xpath).click()
