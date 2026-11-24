import allure

from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Выполнить вход зарегистрированным пользователем')
    def login(self, user):
        self.fill(LoginLocators.EMAIL, user.email)
        self.fill(LoginLocators.PASSWORD, user.password)
        self.click(LoginLocators.SUBMIT)

    @allure.step('Проверить переход на страницу авторизации')
    def is_open(self):
        return self.has_path('/signin')

    @allure.step('Проверить отображение формы авторизации')
    def form_is_visible(self):
        return all(self.visible(locator).is_displayed() for locator in (
            LoginLocators.HEADING, LoginLocators.FORM, LoginLocators.EMAIL,
            LoginLocators.PASSWORD, LoginLocators.SUBMIT,
        ))
