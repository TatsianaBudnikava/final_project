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
    