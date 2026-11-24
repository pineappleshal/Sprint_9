import allure

from locators.recipe_locators import RecipeDetailsLocators
from pages.base_page import BasePage


class RecipeDetailsPage(BasePage):
    @allure.step('Проверить открытие карточки созданного рецепта')
    def is_open(self):
        self.wait_for_recipe_url()
        return self.visible(RecipeDetailsLocators.NAME).is_displayed()

    @allure.step('Получить название рецепта из карточки')
    def get_name(self):
        return self.visible(RecipeDetailsLocators.NAME).text
