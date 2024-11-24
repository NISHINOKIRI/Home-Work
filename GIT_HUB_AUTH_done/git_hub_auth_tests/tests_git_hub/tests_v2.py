import pytest
import allure
from pathlib import Path

nickname = '-' # Заменить на свой логин

@allure.epic('GitHub API')
class Testing_Git_Auth:

    @classmethod
    def clear_allure_results(cls):
        allure_results_path = Path('allure-results')
        # Удаляем все файлы в папке allure-results
        [file.unlink() for file in allure_results_path.iterdir() if file.is_file()]
        print('Файлы предыдущей сессии удалены')

    @pytest.fixture(scope='session', autouse=True)
    def pytest_sessionstart(session):
        with allure.step('Очистка предыдущих результатов...'):
            Testing_Git_Auth.clear_allure_results()
            print('Очистка результатов прошла успешно!')

    @pytest.fixture(autouse=True)
    def setup_class(self, session_auth):
        with allure.step('Настройка авторизации'):
            self.session = session_auth
            allure.attach('Авторизация успешно настроена', name='Статус авторизации', attachment_type=allure.attachment_type.TEXT)

    @allure.story('Статус-код авторизации')
    def test_user_authentication_status_code(self):
        with allure.step('Проверка статус-кода ответа'):
            status_code = self.session.status_code
            allure.attach(f'{status_code}', name='Статус-код', attachment_type=allure.attachment_type.TEXT)
            assert status_code == 200, f'Ошибка: статус-код запроса к API - {status_code}. Ожидался 200.'
            with allure.step('Статус-код авторизации'):
                allure.attach('Статус-код авторизации = 200!', name='PASS', attachment_type=allure.attachment_type.TEXT)

    @allure.story('Проверка данных пользователя')
    def test_user_data_is_not_None(self):
        with allure.step('Данные пользователя'):
            user_data = self.session.user_data
            assert user_data is not None, 'Ошибка: self.session.user_data = None. Авторизация не прошла успешно.'
            with allure.step('Данные пользователя получены?'):
                allure.attach('Данные пользователя успешно получены!', name='RESULT_USER_GET_INFO', attachment_type=allure.attachment_type.JSON)

            user_data_dict = {
                'login': user_data.get('login'),
                'id': user_data.get('id'),
                'followers': user_data.get('followers'),
                'following': user_data.get('following'),
                'public_repos': user_data.get('public_repos'),
                'created_at': user_data.get('created_at'),
                'updated_at': user_data.get('updated_at'),
                'type': user_data.get('type'),
                'plan': user_data['plan']['name']
            }

            user_data_str = '\n'.join(f'{key}: {value}' for key, value in user_data_dict.items() if key != 'plan')
            with allure.step('Наличие данных пользователя'):
                allure.attach(user_data_str, name='Данные пользователя', attachment_type=allure.attachment_type.TEXT)

            links_str = f"avatar: {user_data.get('avatar_url')}\nprofile: {user_data.get('html_url')}"
            with allure.step('Наличие ссылок на аватар и профиль'):
                allure.attach(links_str, name='Ссылки', attachment_type=allure.attachment_type.TEXT)

            with allure.step('Отображение подписочной модели'):
                allure.attach(f'Используемая подписочная модель: {user_data["plan"]["name"]}', name='Подписочная модель', attachment_type=allure.attachment_type.TEXT)

    @allure.story('Проверка поля "login"')
    def test_user_login(self):
        with allure.step('Проверка наличия поля "login"'):
            user_data = self.session.user_data
            assert 'login' in user_data, 'Ошибка: self.session.user_data не содержит поле "login".'

            login_value = user_data.get('login')
            expected_login = nickname

            with allure.step('login_value != None'):
                assert login_value is not None, 'Ошибка: login_value = None. Логин не найден.'
                allure.attach(f'Значение login_value: {login_value}', name='Значение логина', attachment_type=allure.attachment_type.TEXT)

            with allure.step('Полученный логин соответствует ожидаемому'):
                assert login_value == expected_login, f'Ошибка: получен неверный логин - {login_value}.'
                allure.attach('Получен ожидаемый логин', name='Соответствие найдено!', attachment_type=allure.attachment_type.TEXT)
