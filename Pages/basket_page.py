from Pages.base_page import BasePage
from Locators.locators import MainPageLocators as LocatorsM
from Locators.locators import ProductPageLocators as LocatorsP
from Locators.locators import BasketPageLocators as LocatorsB


class BasketPage(BasePage):

    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        assert self.element_is_clickable(LocatorsM.BUTTON_BASKET), 'NotFindButtonBasket'
        self.element_is_clickable(LocatorsM.BUTTON_BASKET).click()
        assert self.is_not_element_present(LocatorsB.EMPTY_OR_NOT_BASKET), 'NotEmptyBasket'
        assert self.element_is_visible(LocatorsB.MESSAGE_EMPTY_BASKET), 'NoText'

    def guest_cant_see_product_in_basket_opened_from_product_page(self):
        assert self.element_is_clickable(LocatorsM.BUTTON_BASKET), 'NotFindButtonBasket'
        self.element_is_clickable(LocatorsM.BUTTON_BASKET).click()
        assert self.is_not_element_present(LocatorsB.EMPTY_OR_NOT_BASKET), 'NotEmptyBasket'
        assert self.element_is_visible(LocatorsB.MESSAGE_EMPTY_BASKET), 'NoText'
