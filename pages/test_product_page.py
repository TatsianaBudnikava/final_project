import pytest
import random

#from basket_page import BasketPage
from base_page import BasePage
from locators import ProductPageLocators
from login_page import LoginPage
from product_page import ProductPage

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.add_to_basket()
    item_page.solve_quiz_and_get_code()
    #item_page.check_item_name() #ЭТИХ МЕТОДОВ НЕТ В ПРОДАКТ ПЕЙДЖЕ
    #item_page.check_price() #ЭТИХ МЕТОДОВ НЕТ В ПРОДАКТ ПЕЙДЖЕ