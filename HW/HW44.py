import requests

response = requests.get('https://api.github.com')

print(f'Статус-код:{response.status_code}')

print(f'Ответ:{response.text}')