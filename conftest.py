import allure
import pytest
from selenium.common.exceptions import WebDriverException

from data import RecipeData, UserData
from helpers.browser_factory import create_browser
from helpers.foodgram_api import FoodgramApi
from pages.header import Header
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.recipe_details_page import RecipeDetailsPage
from pages.recipe_form_page import RecipeFormPage
from pages.signup_page import SignupPage


def pytest_addoption(parser):
    parser.addoption('--headed', action='store_true', help='Показывать окно Chrome')


@pytest.fixture
def driver(request):
    browser = create_browser(headed=request.config.getoption('--headed'))
    yield browser
    browser.quit()


@pytest.fixture
def user_data():
    user = UserData.unique()
    yield user
    api = FoodgramApi()
    try:
        api.cleanup(user)
    finally:
        api.close()


@pytest.fixture
def registered_user(user_data):
    api = FoodgramApi()
    try:
        api.register(user_data)
    finally:
        api.close()
    return user_data


@pytest.fixture
def header(driver):
    return Header(driver).open()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def signup_page(driver):
    return SignupPage(driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def recipe_form_page(driver):
    return RecipeFormPage(driver)


@pytest.fixture
def recipe_details_page(driver):
    return RecipeDetailsPage(driver)


@pytest.fixture
def authorized_header(header, login_page, registered_user, driver):
    header.open_login()
    login_page.login(registered_user)
    MainPage(driver).is_open()
    return header


@pytest.fixture
def recipe_data():
    return RecipeData()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    driver = item.funcargs.get('driver')
    if report.failed and driver is not None:
        try:
            allure.attach(driver.get_screenshot_as_png(), 'Страница при ошибке', allure.attachment_type.PNG)
        except WebDriverException:
            allure.attach('Скриншот недоступен: браузер или модальное окно блокирует получение изображения.',
                          'Диагностика браузера', allure.attachment_type.TEXT)
