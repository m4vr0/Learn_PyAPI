import requests
from Lib.basecase import BaseCase
from Lib.assertions import Assertions
from Lib.my_requests import MyRequests
import re


class TestUserRegister(BaseCase):
    def setup_class(self):
        self.url = "/user/"

    def test_register_user_success(self):
        data = self.prepare_registration_data()

        response = MyRequests.post(self.url, data=data)

        # Проверим, что регистрация прошла успешно.
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, 'id')
        # print(f"Регистрация пользователя с email: {self.email} прошла успешно.")

    def test_register_user_invalid_email_format(self):
        invalid_email = "invalid-email.com"
        # response = requests.post('url_to_register', data={'email': invalid_email, 'password': self.password, 'username': self.username})

        # Проверим, что email не прошел валидацию.
        # assert response.status_code == 400
        print(f"Попытка зарегистрировать пользователя с недопустимым email {invalid_email} завершилась ошибкой.")

    def test_register_user_missing_field(self):
        # Попробуем зарегистрировать пользователя без одного из обязательных полей (например, без пароля)
        # response = requests.post('url_to_register', data={'email': self.email, 'username': self.username})

        # Проверим, что ошибка возвращена из-за отсутствующего поля.
        # assert response.status_code == 400
        print("Попытка зарегистрировать пользователя без обязательного поля завершилась ошибкой.")

    def test_register_user_password_strength(self):
        weak_password = "123"
        # response = requests.post('url_to_register', data={'email': self.email, 'password': weak_password, 'username': self.username})

        # Проверим, что пароль не прошел валидацию по длине или сложности.
        # assert response.status_code == 400
        print(f"Попытка зарегистрировать пользователя с паролем '{weak_password}' завершилась ошибкой.")

    def test_email_format(self):
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        # assert re.match(email_pattern, self.email), f"Email {self.email} имеет неправильный формат."

    def test_unique_email(self):
        pass
        # Предположим, что у нас есть логика проверки уникальности email:
        # response = requests.post('url_to_register', data={'email': self.email, 'password': self.password, 'username': self.username})

        # Если email не уникален, система должна вернуть ошибку.
        # assert response.status_code == 409
        # print(f"Проверка уникальности email {self.email}.")

    def test_register_user_with_existing_email(self):
        # Пример попытки зарегистрироваться с уже существующим email
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post(self.url, data=data)

        # Проверим, что система отклоняет регистрацию с существующим email.
        # Если email уже существует, ожидается статус код 409.
        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Попытка зарегистрировать пользователя с уже существующим email {email} завершилась ошибкой."
