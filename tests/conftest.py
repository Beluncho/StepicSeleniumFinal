import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Chose language: ru, en, ... (etc.)')


@pytest.fixture(scope="function")
def driver(request):
    driver_service = Service(ChromeDriverManager().install())  # is in cache
    user_language = request.config.getoption('language')
    print('\nstart browser for test')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    driver = webdriver.Chrome(service=driver_service, options=options)  # Chrome browser
    driver.implicitly_wait(10)
    driver.maximize_window()  # open full screen
    yield driver
    driver.quit()  # close browser