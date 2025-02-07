import pytest
import requests
from Lib.basecase import BaseCase


class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup_class(self):
        print("\nInit tests...\nTesting ")
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        login_response = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        self.auth_sid = self.get_cookie(response=login_response, cookie_name="auth_sid")
        self.csrf_token = self.get_header(login_response, "x-csrf-token")
        self.user_id_from_auth = self.get_json_value(login_response, "user_id")

    def teardown_class(self):
        print("\nTeardown...")

    def test_auth_user(self):
        chk_auth_response = requests.get(
            url="https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.csrf_token},
            cookies={"auth_sid": self.auth_sid}
        )

        assert "user_id" in chk_auth_response.json(), f"There is no user id in the Check Auth Response"

        user_id_from_chk = chk_auth_response.json()["user_id"]

        assert self.user_id_from_auth == user_id_from_chk, f"User id from Auth method is not equal to user id from Check Auth method"

    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookie":
            response = requests.get(
                url="https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": self.csrf_token}
            )
        else:
            response = requests.get(
                url="https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )

        assert "user_id" in response.json(), f"There is no user id in the Response"

        user_id_from_chk = response.json()["user_id"]

        assert user_id_from_chk == 0, f"User is authorized with condition {condition}"
