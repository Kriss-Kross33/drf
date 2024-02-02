import requests

product_id = input('What is the product id: \n')
try:
    product_id = int(product_id)
except:
    print(f'{product_id} is not a valid product id')

endpoint = f'http://localhost:9999/api/products/{product_id}/delete/'

get_response = requests.delete(endpoint)
print(get_response.status_code, get_response.status_code==204)