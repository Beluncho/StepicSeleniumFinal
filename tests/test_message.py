import pytest

from Pages.product_page import ProductPage


link = ('https://selenium1py.pythonanywhere.com/ru/catalogue'   
        '/coders-at-work_207')


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    """
    is_not_element_present(BasePage)
    :param driver: conftest.py
    :return:
    """
    page_product = ProductPage(driver, link)
    page_product.open()
    page_product.quest_cant_see_success_message_add_until()


def test_guest_cant_see_success_message(driver):
    """
    is_not_element_present(BasePage)
    :param driver: conftest.py
    :return:
    """
    page_product = ProductPage(driver, link)
    page_product.open()
    page_product.quest_cant_see_success_message_until_without_add()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    """
    is_disappeared(BasePage)
    :param driver: conftest.py
    :return:
    """
    page_product = ProductPage(driver, link)
    page_product.open()
    page_product.quest_cant_see_success_message_add_until_not()

