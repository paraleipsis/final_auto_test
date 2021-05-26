from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME).text
        name_message = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert self.browser.find_element(*ProductPageLocators.MESSAGE), 'No message'
        assert product_name == name_message, 'Titles does not match'
        assert price == message_price, 'Prices does not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Message is not disappeared"
