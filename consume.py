import requests

response = requests.get('http://127.0.0.1:7000')
print(response.json())