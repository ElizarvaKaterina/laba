import json

with open('data.json') as jsonfile:
    data = json.load(jsonfile)

products = data['products']

for product in products:
    name = product['name']
    price = product['price']
    weight = product['weight']
    available = product['available']

    print(f"Название: {name}")
    print(f"Цена: {price}")
    print(f"Вес: {weight}")

    if available:
        print("В наличии")
    else:
        print("Нет в наличии!")

    print()
