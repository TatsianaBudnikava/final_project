from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REG_FORM = (By.ID, 'register_form') 
    
    LOG_email = (By.ID, "id_login-username")
    LOG_password = (By.ID, "id_login-password") 
    SUBMIT_button = (By.NAME, "login_submit")    
    
    
    REG_email = (By.ID, "id_registration-email")
    REG_password = (By.ID, "id_registration-password1")
    REG_password_repeating = (By.ID, "id_registration-password2")
    SUBMIT_button = (By.NAME, "registration_submit")  
    
    
class ProductPageLocators():

    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini>span>a')
    EMPTY_BASKET = (By.ID, "content_inner")
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]//p[contains(text(),"Your basket is empty.")]')
