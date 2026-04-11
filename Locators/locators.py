from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BUTTON_BASKET = (By.XPATH, "//a[@class='btn btn-default']")


class LoginPageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    ENTER_REGISTRATION_BUTTON = (By.XPATH, "//a[@id= 'login_link']")
    REGISTRATION_LOGIN = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REPEAT_REGISTRATION_PASSWORD = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@name= 'registration_submit']")


class ProductPageLocators:
    ADD_PROD = (By.CSS_SELECTOR, 'button.btn-add-to-basket')

    NAME_PROD_ADD = (By.XPATH, "//div[@class= 'alertinner ']//strong")

    NAME_PROD = (By.XPATH, "//div[@class= 'col-sm-6 product_main']//h1")

    PRICE_PROD_ADD = (By.XPATH, "//div[@class= 'alert alert-safe alert-noicon"
                            " alert-info  fade in']//strong")

    PRICE_PROD = (By.XPATH, "//div[@class= 'col-sm-6 product_main']//p")

    MESSAGE = (By.ID, "messages")


class BasketPageLocators:
    EMPTY_OR_NOT_BASKET = (By.XPATH, "//form[@class= 'basket_summary']")
    MESSAGE_CONTAIN = (By.ID, "#content_inner")
    MESSAGE_EMPTY_BASKET = (By.XPATH, "//div[@id= 'content_inner']//p")
