import os
from datetime import datetime
from requests import Response


class Logger:
    file_name = f"logs/log_{str(datetime.now().strftime('%d-%m-%Y_%H-%M-%S'))}.log"

    @classmethod
    def _write_log_to_file(cls, data: str):
        with open(cls.file_name, "a", encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, data: dict, headers: dict, cookies: dict, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Data: {str(datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"Request DATA: {data}\n"
        data_to_add += f"Request HEADERS: {headers}\n"
        data_to_add += f"Request COOKIES: {cookies}\n"
        data_to_add += f"\n"

        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        data_to_add = f"Response CODE: {response.status_code}\n"
        data_to_add += f"Response TEXT: {response.status_code}\n"
        data_to_add += f"Response HEADERS: {headers_as_dict}\n"
        data_to_add += f"Response COOKIES: {cookies_as_dict}\n"
        data_to_add += f"\n-----\n"

        cls._write_log_to_file(data_to_add)
