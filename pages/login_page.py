from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        
    def should_be_login_url(self):
        """Проверяем, что текущая ссылка это содержит login"""
        assert self.browser.current_url.find("login") != 0, "Is not login url"


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        result = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert result

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        result = self.is_element_present(*LoginPageLocators.REG_FORM)
        assert result
        
    def go_to_login_page(self):
       link = self.browser.find_element_by_css_selector("#login_link")
       link.click()
       alert = self.browser.switch_to.alert
       alert.accept()    