from .base_page import BasePage
from .locators import 


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, f"expected 'login' to be substring of '{self.browser.current_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASS_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
