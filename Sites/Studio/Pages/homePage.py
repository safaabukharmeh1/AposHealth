from Sites.Studio.Locators.locators import Locators

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_arrow_xpath = Locators.logout_arrow_xpath
        self.logoutlink_text = Locators.logoutlink_text

    def click_arrow(self, driver):
        self.driver.find_element_by_xpath(self.logout_arrow_xpath).click()

    def click_logout(self,driver):
        self.driver.find_element_by_link_text(self.logoutlink_text).click()
