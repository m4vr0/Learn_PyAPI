from datetime import datetime
import requests


class TestUserRegister:
    def setup_class(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")

        self.url = "https://playground.learnqa.ru/api/user/"

        self.email = f"{base_part}{random_part}@{domain}"
        self.password = "TestPassword123"
        self.username = "TestUser"

    def test_register_user_success(self):
        data = {
            
        }


        response = requests.post('url', data=self.)

        # Проверим, что регистрация прошла успешно.
        # assert response.status_code == 200
        print(f"Регистрация пользователя с email: {self.email} прошла успешно.")

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
        assert re.match(email_pattern, self.email), f"Email {self.email} имеет неправильный формат."

    def test_unique_email(self):
        # Предположим, что у нас есть логика проверки уникальности email:
        # response = requests.post('url_to_register', data={'email': self.email, 'password': self.password, 'username': self.username})

        # Если email не уникален, система должна вернуть ошибку.
        # assert response.status_code == 409
        print(f"Проверка уникальности email {self.email}.")

    def test_register_user_with_existing_email(self):
        # Пример попытки зарегистрироваться с уже существующим email
        # response = requests.post('url_to_register', data={'email': self.existing_email, 'password': self.password, 'username': self.username})

        # Проверим, что система отклоняет регистрацию с существующим email.
        # Если email уже существует, ожидается статус код 409.
        # assert response.status_code == 409
        print(
            f"Попытка зарегистрировать пользователя с уже существующим email {self.existing_email} завершилась ошибкой.")
