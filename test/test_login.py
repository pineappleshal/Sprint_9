import allure

@allure.feature('Авторизация')
class TestLogin:
    @allure.title('После входа открывается главная страница и видна кнопка «Выход»')
    def test_login_opens_main_page(self, header, login_page, main_page, registered_user):
        header.open_login()
        login_page.login(registered_user)

        assert main_page.is_open(), 'После входа должна открыться страница /recipes'
        assert header.logout_is_visible(), 'После входа должна отображаться кнопка «Выход»'
