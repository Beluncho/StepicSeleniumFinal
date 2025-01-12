import time

from Pages.base_page import BasePage
from Locators.locators import LoginPageLocators as locators
import faker


class LoginPage(BasePage):

    def register_new_user(self):
        fake = faker.Faker()
        mail = fake.email()
        password = fake.password()
        assert self.element_is_clickable(locators.ENTER_REGISTRATION_BUTTON), 'NoEnterRegistrationButton'
        self.element_is_clickable(locators.ENTER_REGISTRATION_BUTTON).click()
        self.element_is_visible(locators.REGISTRATION_LOGIN).send_keys(mail)
        self.element_is_visible(locators.REGISTRATION_PASSWORD).send_keys(password)
        self.element_is_visible(locators.REPEAT_REGISTRATION_PASSWORD).send_keys(password)
        self.element_is_clickable(locators.REGISTRATION_BUTTON).click()
        assert self.should_be_authorized_user(locators.USER_ICON), ('User icon is not presented,'
                                                                    'probably unauthorised user')

    def guest_can_go_to_login_page_from_product_page(self):
        assert self.element_is_clickable(locators.ENTER_REGISTRATION_BUTTON), 'NoEnterRegistrationButton'
        self.element_is_clickable(locators.ENTER_REGISTRATION_BUTTON).click()
        assert self.driver.current_url == "https://selenium1py.pythonanywhere.com/ru/accounts/login/"

