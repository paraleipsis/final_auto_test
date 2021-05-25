from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "#login_form")
    REG = (By.CSS_SELECTOR, "#register_form")