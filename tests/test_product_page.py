import pytest

from Pages.product_page import ProductPage
from Pages.basket_page import BasketPage
from Pages.login_page import LoginPage


"""
pytest -v --pyargs --tb=line --language=en -m need_review

Пожалуйста используйте такой код для проверки,
(--pyargs) - для запуска при разработке в Пиче,
лечит ошибку ModuleNotFoundError: No module named 'Pages'
"""
link = ('https://selenium1py.pythonanywhere.com/ru/catalogue' 
        '/coders-at-work_207')


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(driver):
    """
    :param driver: conftest.py
    :param link: from fixture, add with fixture
    :return:
    """
    page_product = ProductPage(driver, link)
    page_product.open()
    page_product.fill_button_add_product_prise_check()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    page_product = BasketPage(driver, link)
    page_product.open()
    page_product.guest_cant_see_product_in_basket_opened_from_product_page()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    page_product = LoginPage(driver, link)
    page_product.open()
    page_product.guest_can_go_to_login_page_from_product_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.user = LoginPage(driver, link)
        self.user.open()
        self.user.register_new_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        """
        :param driver: conftest.py
        :return:
        """
        page_product = ProductPage(driver, link)
        page_product.open()
        page_product.fill_button_add_product_prise_check()

    @pytest.mark.skip
    def test_user_cant_see_success_message(self, driver):
        """
        is_not_element_present(BasePage)
        :param driver: conftest.py
        :return:
        """
        page_product = ProductPage(driver, link)
        page_product.open()
        page_product.quest_cant_see_success_message_until_without_add()
