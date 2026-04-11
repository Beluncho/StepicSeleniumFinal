# 🧪 Stepic Selenium Final Project

Автотесты для интернет-магазина [selenium1py.pythonanywhere.com](https://selenium1py.pythonanywhere.com/).

Финальный проект курса по автоматизации тестирования на Stepik.

## 🎯 Что тестируется

| Сценарий | Описание |
|----------|----------|
| **Добавление товара в корзину** | Проверка, что название и цена товара совпадают с добавленными |
| **Регистрация пользователя** | Создание нового пользователя через форму регистрации |
| **Переход на страницу логина** | Проверка перехода с главной страницы и со страницы товара |
| **Пустая корзина** | Проверка, что в корзине нет товаров у гостя |
| **Сообщения после добавления** | Проверка появления/исчезновения сообщений |

## 🛠 Технологии

| Технология | Назначение |
|------------|------------|
| Python 3 | Язык программирования |
| Selenium WebDriver | Управление браузером |
| Pytest | Запуск и организация тестов |
| Page Object Model | Паттерн для работы со страницами |
| Faker | Генерация тестовых данных |

## 📁 Структура проекта
```
StepicSeleniumFinal/
├── Pages/ # Page Object классы
│ ├── base_page.py # Базовый класс с общими методами
│ ├── main_page.py # Главная страница
│ ├── login_page.py # Страница логина/регистрации
│ ├── product_page.py # Страница товара
│ └── basket_page.py # Корзина
├── Locators/ # Локаторы элементов
│ └── locators.py # Все локаторы в одном файле
├── tests/ # Тесты
│ ├── test_main_page.py # Тесты главной страницы
│ ├── test_product_page.py # Тесты страницы товара
│ └── test_message.py # Тесты сообщений
├── conftest.py # Фикстуры и настройка драйвера
├── pytest.ini # Настройки Pytest (маркеры)
├── requirements.txt # Зависимости
└── README.md # Этот файл
```
## ▶️ Запуск тестов

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Запуск всех тестов
```bash
pytest -v
```
### 3. Запуск с определённым языком
```bash
pytest --language=ru -v
pytest --language=en -v
```
### 4. Запуск только маркированных тестов
```bash
pytest -m need_review -v
```
### 5. Запуск с подробным выводом ошибок
```bash
pytest -v --tb=line
```
### 6. Запуск через PyCharm (если ошибка ModuleNotFoundError)
```bash
pytest -v --pyargs --tb=line --language=en -m need_review
```
# 📊 Пример вывода
```bash
$ pytest -v

==================== test session starts ====================
test_main_page.py::test_guest_can_go_to_login_page PASSED
test_main_page.py::test_guest_should_see_login_link PASSED
test_main_page.py::test_guest_cant_see_product_in_basket_opened_from_main_page PASSED
test_product_page.py::test_guest_can_add_product_to_basket PASSED
test_product_page.py::test_guest_cant_see_product_in_basket_opened_from_product_page PASSED
test_product_page.py::test_guest_can_go_to_login_page_from_product_page PASSED
test_product_page.py::TestUserAddToBasketFromProductPage::test_user_can_add_product_to_basket PASSED
==================== 7 passed in 45.23s ====================
```
# 🔧 Ключевые методы BasePage
python
## Ожидание видимости элемента
```
def element_is_visible(self, locator, timeout=5):
    return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
```
## Проверка, что элемента НЕТ
```
def is_not_element_present(self, locator, timeout=4):
    try:
        Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        return True
    return False
```

## Проверка, что элемент исчез
```
def is_disappeared(self, locator, timeout=4):
    try:
        Wait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))
    except TimeoutException:
        return False
    return True
```

# Решение математического квиза (alert)
```
def solve_quiz_and_get_code(self):
    alert = self.driver.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
```

# 🔄 Планы по улучшению
Добавить Allure-отчёты

Запуск в GitHub Actions (CI/CD)

Добавить тесты на API

Разделить локаторы по страницам (сейчас всё в одном файле)

Добавить скриншоты при падении тестов
