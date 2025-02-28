import json
from requests import Response
from typing import Any

class Assertions:
    @staticmethod
    def __get_json(response: Response) -> dict:
        """
        Вспомогательный метод для проверки и парсинга JSON-ответа.

        Принимает объект Response, пытается преобразовать его в JSON.
        В случае невалидного JSON вызывает ошибку assert.

        :param response: HTTP-ответ в формате Response
        :return: Распарсенный JSON в виде словаря
        """
        try:
            return response.json()
        except json.JSONDecodeError:
            assert False, f"Response was not valid JSON: {response.text}"

    @staticmethod
    def assert_json_value_by_name(response: Response, name: str, expected_value: Any, error_message: str) -> None:
        """
        Проверяет, что в JSON-ответе присутствует указанный ключ и его значение соответствует ожидаемому.

        :param response: HTTP-ответ в формате Response
        :param name: Имя ключа в JSON
        :param expected_value: Ожидаемое значение ключа
        :param error_message: Сообщение об ошибке, если значение не соответствует ожидаемому
        """
        Assertions.assert_json_has_key(response, name)
        response_as_dict = Assertions.__get_json(response)

        assert response_as_dict[name] == expected_value, f"{error_message}. Got: {response_as_dict[name]}"

    @staticmethod
    def assert_json_has_key(response: Response, name: str) -> None:
        """
        Проверяет, что в JSON-ответе присутствует указанный ключ.

        :param response: HTTP-ответ в формате Response
        :param name: Имя ключа, который должен присутствовать в JSON
        """
        response_as_dict = Assertions.__get_json(response)

        assert name in response_as_dict, f"{name} was not found in response"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list) -> None:
        """
        Проверяет, что в JSON-ответе присутствует указанный ключ.

        :param response: HTTP-ответ в формате Response
        :param names: Список имён ключей, которые должны присутствовать в JSON
        """
        response_as_dict = Assertions.__get_json(response)

        for name in names:
            assert name in response_as_dict, f"{name} was not found in response"

    @staticmethod
    def assert_json_has_not_key(response: Response, name: str) -> None:
        """
        Проверяет, что в JSON-ответе присутствует указанный ключ.

        :param response: HTTP-ответ в формате Response
        :param name: Имя ключа, который должен присутствовать в JSON
        """
        response_as_dict = Assertions.__get_json(response)

        assert name not in response_as_dict, (f"Response shouldn't have key {name} but it's was found in response")

    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list) -> None:
        """
        Проверяет, что в JSON-ответе присутствует указанный ключ.

        :param response: HTTP-ответ в формате Response
        :param names: Список имён ключей, которые должны присутствовать в JSON
        """
        response_as_dict = Assertions.__get_json(response)

        for name in names:
            assert name not in response_as_dict, f"Response shouldn't have key {name} but it's was found in response"

    @staticmethod
    def assert_status_code(response: Response, expected_status: int) -> None:
        """
        Проверяет, что код состояния HTTP-ответа соответствует ожидаемому значению.

        :param response: HTTP-ответ в формате Response
        :param expected_status: Ожидаемый код состояния HTTP
        """
        assert response.status_code == expected_status, f"Expected status code {expected_status}, but got {response.status_code}"