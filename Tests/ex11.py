import requests


class TestCookie:
    def setup_class(self):
        self.url = 'https://playground.learnqa.ru/api/homework_cookie'

        response = requests.get(self.url)

        self.cookies = response.cookies.get_dict()

    def test_cookie(self):
        assert len(self.cookies) > 0, "Cookies are empty"
        print(f"Cookie name is {list(self.cookies.keys())[0]}\nCokie valuue is {list(self.cookies.values())[0]}")
