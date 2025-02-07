import pytest
import requests


class TestFirstAPI:
    names = [
        ("Vitalii"),
        ("Arsenij"),
        ("")
    ]

    @pytest.mark.parametrize("name", names)
    def test_hello_call(self, name):
        url = 'https://playground.learnqa.ru/api/hello'
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()

        assert "answer" in response_dict, "There is no field 'answer' in the Response"

        if not len(name):
            expected_response_text = f"Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, f"Actual text in the Response is not correct"
