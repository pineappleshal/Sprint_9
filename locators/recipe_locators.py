from selenium.webdriver.common.by import By


class RecipeFormLocators:
    NAME = (By.XPATH, '//label[.//div[normalize-space()="Название рецепта"]]//input')
    BREAKFAST = (By.XPATH, '//div[span[normalize-space()="Завтрак"]]/button')
    LUNCH = (By.XPATH, '//div[span[normalize-space()="Обед"]]/button')
    DINNER = (By.XPATH, '//div[span[normalize-space()="Ужин"]]/button')
    INGREDIENT = (By.XPATH, '//label[.//div[normalize-space()="Ингредиенты"]]//input')
    SALT_SUGGESTION = (By.XPATH, '//div[normalize-space()="соль" and not(*)]')
    AMOUNT = (By.CSS_SELECTOR, 'input[class*="ingredientsAmountValue"]')
    ADD_INGREDIENT = (By.XPATH, '//div[normalize-space()="Добавить ингредиент" and not(*)]')
    ADDED_INGREDIENT = (By.CSS_SELECTOR, '[class*="ingredientsAddedItemTitle"]')
    COOKING_TIME = (By.XPATH, '//label[.//div[normalize-space()="Время приготовления"]]//input')
    DESCRIPTION = (By.TAG_NAME, 'textarea')
    IMAGE = (By.CSS_SELECTOR, 'input[type="file"]')
    IMAGE_PREVIEW = (By.CSS_SELECTOR, '[style*="data:image/"]')
    SUBMIT = (By.XPATH, '//button[normalize-space()="Создать рецепт"]')


class RecipeDetailsLocators:
    NAME = (By.TAG_NAME, 'h1')
    EDIT = (By.LINK_TEXT, 'Редактировать рецепт')
