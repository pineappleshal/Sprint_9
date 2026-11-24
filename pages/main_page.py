import allure

from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Проверить переход на главную страницу рецептов')
    def is_open(self):
        return self.has_path('/recipes') and self.visible(MainLocators.HEADING).is_displayed()
