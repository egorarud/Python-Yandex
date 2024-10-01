import requests

base_url = 'https://fakestoreapi.com'

#1 Вывести продукты, цена которых <20

response = requests.get(f'{base_url}/products')
products = response.json()
filtered_products = [product for product in products if product["price"] < 20]
print(filtered_products)

#2 Вывести все категории

response = requests.get(f'{base_url}/products/categories')
categories = response.json()
print(categories)

#3 Вывести все продукты с категорией  "jewelery"

response = requests.get(f'{base_url}/products/category/jewelery')
jewelery_products = response.json()
print(jewelery_products)


#4 Вывести всех пользователей

response = requests.get(f'{base_url}/users/1')
users = response.json()
print(users)

# 5 Добавить пользователя со своим именем.

my_user = {
    'address': {
        'geolocation': {
            'lat': '0', 'long': '0'
        }, 
        'city': 'ekb', 
        'street': 'st', 
        'number': 0, 
        'zipcode': '0'
    }, 
    'id': 1111, 
    'email': '0', 
    'username': 'egora', 
    'password': '1111', 
    'name': {
        'firstname': 'egor', 
        'lastname': 'rud'
    }, 
    'phone': '0', 
    '__v': 0
}

response = requests.post(f'{base_url}/users', json = my_user)
print(response.status_code)