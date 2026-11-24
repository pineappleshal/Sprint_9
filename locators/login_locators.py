from selenium.webdriver.common.by import By


class LoginLocators:
    FORM = (By.TAG_NAME, 'form')
    HEADING = (By.XPATH, '//h1[normalize-space()="Войти на сайт"]')
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    SUBMIT = (By.XPATH, '//button[normalize-space()="Войти"]')
