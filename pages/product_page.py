from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage
from locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        try:
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
            return True
        except NoSuchElementException:
            return False
