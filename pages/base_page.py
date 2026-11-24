import re

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL, WAIT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    def open(self, path='/'):
        self.driver.get(BASE_URL + path)
        return self

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator, value):
        element = self.visible(locator)
        element.clear()
        element.send_keys(value)

    def set_toggle(self, locator, selected):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        active = 'checkbox_active' in element.get_attribute('class')
        if active != selected:
            element.click()

    def has_path(self, path):
        self.wait.until(EC.url_to_be(BASE_URL + path))
        return self.driver.current_url == BASE_URL + path

    def wait_for_recipe_url(self):
        self.wait.until(EC.url_matches(re.escape(BASE_URL) + r'/recipes/\d+/?$'))
        return self.driver.current_url

    def upload(self, locator, path):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(str(path.resolve()))
