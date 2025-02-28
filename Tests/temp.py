class Assertions:
    @staticmethod
    def assert_json_has_keys(response, expected_keys):
        try:
            response_as_dict = response.json()
        except ValueError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        for key in expected_keys:
            assert key in response_as_dict, f"Expected key '{key}' is missing from JSON response"

    @staticmethod
    def assert_code_status(response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"

    @staticmethod
    def assert_json_has_key(response, name):
        try:
            response_as_dict = response.json()
        except ValueError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict,