import requests

endpoint = 'http://localhost:9999/api/products/1/'

get_response = requests.get(endpoint)
print(get_response.json())