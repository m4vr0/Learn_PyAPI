import requests
from Lib.my_requests import MyRequests
from Lib.basecase import BaseCase
from Lib.assertions import Assertions


class TestUserGet(BaseCase):
    def setup_class(self):
        pass

    def test_get_user_details_not_auth(self):
        response = MyRequests.get('/user/2')
        print(response.content)
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    def test_get_user_details_auth_as_same_user(self):
        uid = 2

        # Авторизация как пользователь с uid=2
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post(f'/user/login', data=login_data)

        # print(f"JSON: {response1.json()}")

        # Проверка успешной авторизации
        Assertions.assert_status_code(response1, 200)
        # Assertions.assert_json_has_key(response1, "auth_sid")
        # Assertions.assert_json_has_key(response1, "x-csrf-token")

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        # Получение данных пользователя с авторизацией
        response2 = MyRequests.get(
            f'/user/{user_id_from_auth_method}',
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        # Проверка, что все ключи присутствуют в ответе
        expected_keys = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_keys)
