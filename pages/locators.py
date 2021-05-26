from selenium.webdriver.common.by import 


class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "#login_form")
    REG = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.ID, 'id_registration-email')
    PASS_FORM = (By.ID, 'id_registration-password1')
    CONFIRM_FORM = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > .btn')


class ProductPageLocators():
    BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    MESSAGE_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner p strong')
    NAME = (By.CSS_SELECTOR, 'h1')
    MESSAGE_NAME = (By.CSS_SELECTOR, 'div.alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages >.alert:first-child > .alertinner')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, '.row > h2')
