import pytest
import random
import time 

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

class TestGuestAddToBasketFromProductPage():
   
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        time.sleep(1)
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()
    
    
    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        """Тест, что гостю не показывается сообщение об успешном добавлении товара при такой попытке"""
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()
        
    
    def test_guest_cant_see_success_message(self, browser):
        """Тест, что гостю не показывается сообщение об успешном добавлении товара при открытии страницы товара"""
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_disappeared_success_message()    
    
    
    def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
    
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()    

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_empty()
 

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        login_page.open()
        # Генерируем почту, прописываем надежный пароль и регистрируем нового пользователя
        email = str(time.time()) + "@fakemail.org"
        password = "final123456"
        # Регистрируем нового пользователя. Он должен автомтически авторизоваться
        login_page.register_new_user(email, password)
        # Проверяем, что пользователь авторизован
        login_page.should_be_authorized_user()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        time.sleep(1)
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()
    
       
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """Тест, что пользователю не показывается сообщение об успешном добавлении товара при такой попытке"""
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()    
        
    