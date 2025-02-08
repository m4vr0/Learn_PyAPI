from typing import Any
import json
from requests import Response


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name: str, expected_value: Any, error_message: str) -> None:
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response was not valid JSON: {response.text}"

        assert name in response_as_dict, f"{name} was not found in response"
        assert response_as_dict[name] == expected_value, error_message
