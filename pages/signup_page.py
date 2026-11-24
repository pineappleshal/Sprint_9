import allure

from locators.signup_locators import SignupLocators
from pages.base_page import BasePage


class SignupPage(BasePage):
    @allure.step('Заполнить регистрационную форму и создать аккаунт')
    def register(self, user):
        self.fill(SignupLocators.FIRST_NAME, user.first_name)
        self.fill(SignupLocators.LAST_NAME, user.last_name)
        self.fill(SignupLocators.USERNAME, user.username)
        self.fill(SignupLocators.EMAIL, user.email)
        self.fill(SignupLocators.PASSWORD, user.password)
        self.click(SignupLocators.SUBMIT)
