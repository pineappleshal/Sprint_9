from dataclasses import asdict

import allure
import requests

from config import API_URL, REQUEST_TIMEOUT


class FoodgramApi:
    def __init__(self):
        self.session = requests.Session()

    def request(self, method, path, **kwargs):
        return self.session.request(method, API_URL + path, timeout=REQUEST_TIMEOUT, **kwargs)

    @allure.step('Создать отдельного пользователя для предусловия через API')
    def register(self, user):
        response = self.request('POST', '/api/users/', json=asdict(user))
        assert response.status_code == 201, f'Регистрация: {response.status_code}, {response.text}'

    @allure.step('Удалить созданные рецепты и закрыть тестовую сессию')
    def cleanup(self, user):
        response = self.request('POST', '/api/auth/token/login/', json={
            'email': user.email, 'password': user.password,
        })
        if response.status_code != 200:
            allure.attach(
                f'Вход для очистки тестовых данных недоступен: {response.status_code}, {response.text}',
                'Очистка тестовых данных', allure.attachment_type.TEXT,
            )
            return
        self.session.headers['Authorization'] = 'Token ' + response.json()['auth_token']
        response = self.request('GET', '/api/users/me/')
        response.raise_for_status()
        user_id = response.json()['id']
        response = self.request('GET', '/api/recipes/', params={'author': user_id, 'limit': 100})
        response.raise_for_status()
        for recipe in response.json()['results']:
            assert recipe['author']['id'] == user_id, 'Рецепт должен принадлежать тестовому пользователю'
            deleted = self.request('DELETE', f'/api/recipes/{recipe["id"]}/')
            assert deleted.status_code == 204, f'Удаление тестового рецепта: {deleted.status_code}'
        response = self.request('POST', '/api/auth/token/logout/')
        assert response.status_code == 204, f'Выход из тестовой сессии: {response.status_code}'

    def close(self):
        self.session.close()
