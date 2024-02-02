import requests
from getpass import getpass

password = getpass()

auth_endpoint = 'http://localhost:9999/api/auth/'
auth_response = requests.post(auth_endpoint, json={'username': 'kriss', 'password': password})

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    print(auth_response.json())
    headers = {'Authorization': f'Bearer {token}'}
    endpoint = 'http://localhost:9999/api/products/'

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())