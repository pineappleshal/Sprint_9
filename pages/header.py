import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):
    @allure.step('Нажать «Создать аккаунт» в шапке')
    def open_signup(self):
        self.click(HeaderLocators.SIGNUP)

    @allure.step('Нажать «Войти» в шапке')
    def open_login(self):
        self.click(HeaderLocators.SIGNIN)

    @allure.step('Открыть вкладку «Создать рецепт»')
    def open_recipe_form(self):
        self.click(HeaderLocators.CREATE_RECIPE)

    @allure.step('Проверить отображение кнопки «Выход»')
    def logout_is_visible(self):
        return self.visible(HeaderLocators.LOGOUT).is_displayed()
