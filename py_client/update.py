import requests

endpoint = 'http://localhost:9999/api/products/1/update/'

data = {
    'title': 'Here is the updated title',
    'price': 399.99
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())