import pytest
import random

#from basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.add_to_basket()
    item_page.solve_quiz_and_get_code()
    #item_page.check_item_name() 
    #item_page.check_price() 
    
