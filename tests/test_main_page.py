from Pages.main_page import MainPage
from Pages.basket_page import BasketPage


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(driver):
    page = MainPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    page = BasketPage(driver, link)
    page.open()
    page.guest_cant_see_product_in_basket_opened_from_main_page()
