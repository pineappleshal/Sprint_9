import allure

from locators.recipe_locators import RecipeFormLocators
from pages.base_page import BasePage


class RecipeFormPage(BasePage):
    @allure.step('Заполнить форму и создать рецепт с фотографией')
    def create(self, recipe):
        self.fill(RecipeFormLocators.NAME, recipe.name)
        self.set_toggle(RecipeFormLocators.BREAKFAST, False)
        self.set_toggle(RecipeFormLocators.LUNCH, True)
        self.set_toggle(RecipeFormLocators.DINNER, False)
        self.fill(RecipeFormLocators.INGREDIENT, recipe.ingredient)
        self.click(RecipeFormLocators.SALT_SUGGESTION)
        self.fill(RecipeFormLocators.AMOUNT, recipe.amount)
        self.click(RecipeFormLocators.ADD_INGREDIENT)
        self.visible(RecipeFormLocators.ADDED_INGREDIENT)
        self.fill(RecipeFormLocators.COOKING_TIME, recipe.cooking_time)
        self.fill(RecipeFormLocators.DESCRIPTION, recipe.description)
        self.upload(RecipeFormLocators.IMAGE, recipe.image_path)
        self.visible(RecipeFormLocators.IMAGE_PREVIEW)
        self.click(RecipeFormLocators.SUBMIT)
