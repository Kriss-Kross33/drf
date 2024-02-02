import requests

endpoint = 'http://localhost:9999/api/products/'

data = {
    "title": "This is the title",
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())