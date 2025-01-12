from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

import math


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(10)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)

        except NoSuchElementException:
            return False
        return True

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=15):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, locator, timeout=4):
        try:
            Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, timeout=4):
        try:
            Wait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


