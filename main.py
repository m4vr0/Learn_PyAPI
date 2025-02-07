import requests

payload = {"login": "secret_login", "password": "secret_pass"}
# response = requests.get('https://playground.learnqa.ru/api/hello', params=payload)
# response = requests.get('https://playground.learnqa.ru/api/get_text')
response = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', data=payload)

cookie_val = response.cookies.get("auth_cookie")
cookies = {}

if cookie_val is not None:
    cookies.update({'auth_cookie': cookie_val})

srespense = requests.post('https://playground.learnqa.ru/api/check_auth_cookie', cookies=cookies)

print(srespense.text)
# print(response.status_code)
# print(dict(response.cookies))
# print(response.headers)
