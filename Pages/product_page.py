from .base_page import BasePage
from Locators.locators import ProductPageLocators as Locators


class ProductPage(BasePage):
    def fill_button_add_product_prise_check(self):
        self.element_is_clickable(Locators.ADD_PROD).click()
        # self.solve_quiz_and_get_code()
        assert (self.element_is_visible(Locators.NAME_PROD_ADD).text ==
                self.element_is_visible(Locators.NAME_PROD).text), 'InvalidProductName'

        assert (self.element_is_visible(Locators.PRICE_PROD_ADD).text ==
                self.element_is_visible(Locators.PRICE_PROD).text), 'InvalidPriseProduct'

    def quest_cant_see_success_message_add_until(self):
        self.element_is_clickable(Locators.ADD_PROD).click()
        assert (self.is_not_element_present(Locators.PRICE_PROD_ADD)), 'FindMessage'

    def quest_cant_see_success_message_until_without_add(self):
        self.element_is_clickable(Locators.ADD_PROD)
        assert (self.is_not_element_present(Locators.PRICE_PROD_ADD)), 'FindMessage'

    def quest_cant_see_success_message_add_until_not(self):
        self.element_is_clickable(Locators.ADD_PROD).click()
        assert (self.is_disappeared(Locators.PRICE_PROD_ADD)), 'MessageDoesNotDisappear'
