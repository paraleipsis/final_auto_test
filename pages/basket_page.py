from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), \
            "Basket is not empty"

    def basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "No basket is empty text"
