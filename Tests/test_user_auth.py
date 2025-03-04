import pytest
from Lib.basecase import BaseCase
from Lib.assertions import Assertions
from Lib.my_requests import MyRequests


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

        login_response = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(self, login_response, "auth_sid")
        self.csrf_token = self.get_header(self, login_response, "x-csrf-token")
        self.user_id_from_auth = self.get_json_value(self, login_response, "user_id")

    def teardown_class(self):
        print("\nTeardown...")

    def test_auth_user(self):
        chk_auth_response = MyRequests.get(
            url="/user/auth",
            headers={"x-csrf-token": self.csrf_token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response=chk_auth_response,
            name="user_id",
            expected_value=self.user_id_from_auth,
            error_message=f"User id from Auth method was not equal to user id from check method"
        )

    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookie":
            response = MyRequests.get(
                url="/user/auth",
                headers={"x-csrf-token": self.csrf_token}
            )
        else:
            response = MyRequests.get(
                url="/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )

        Assertions.assert_json_value_by_name(
            response=response,
            name="user_id",
            expected_value=0,
            error_message=f"User is authorized with condition {condition}"
        )
