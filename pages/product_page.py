from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        try:
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
            return True
        except NoSuchElementException:
            return False

    def get_product_name(self):
        try:
            return str(self.browser.find_element(*ProductPageLocators.ITEM_NAME).text)
        except NoSuchElementException:
            return None
            
            
    def should_be_message_about_adding(self):
        """Проверяем сообщение о добавлении товара"""
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), ("Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), ("Message about adding is not presented")
        product_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text + " has been added to your basket."
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == message, "No product name in the message"

    def should_be_message_basket_total(self):
        """Проверяем цену товара добавленную в корзину"""
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE), ("Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRICE), ("Product price is not presented") 
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price in price_message, "No product price in the message"
        

    def should_not_be_success_message(self):
        """Ожидаем, что сообщение о добавлении не появится"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    def should_be_disappeared_success_message(self):
        """Ожидаем, что сообщение о добавлении исчезнет"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should be disappeared"
   

    def get_price(self):
        try:
            return str(self.browser.find_element(*ProductPageLocators.PRICE).text)
        except NoSuchElementException:
            return None

   
    def check_price(self):
        price = self.get_price()
        price_message = self.get_price_from_message()
        assert price == price_message, 'Price does not match with expected'
        
        
    def go_to_basket_page(self):  
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_link.click()      