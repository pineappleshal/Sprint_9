from selenium.webdriver.common.by import By


class HeaderLocators:
    SIGNUP = (By.LINK_TEXT, 'Создать аккаунт')
    SIGNIN = (By.LINK_TEXT, 'Войти')
    CREATE_RECIPE = (By.LINK_TEXT, 'Создать рецепт')
    LOGOUT = (By.XPATH, '//header//a[normalize-space()="Выход"]')
