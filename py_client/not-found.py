import requests

endpoint = 'http://localhost:9999/api/products/23423423423/'

get_response = requests.get(endpoint)
print(get_response.json())