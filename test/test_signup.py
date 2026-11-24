import allure

@allure.feature('Создание аккаунта')
class TestSignup:
    @allure.title('После регистрации открывается страница с формой авторизации')
    def test_signup_opens_login_form(self, header, signup_page, login_page, user_data):
        header.open_signup()
        signup_page.register(user_data)

        assert login_page.is_open(), 'После регистрации должна открыться страница /signin'
        assert login_page.form_is_visible(), 'Форма авторизации должна отображаться полностью'
