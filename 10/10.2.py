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

new_product = {}
new_product['name'] = input("Введите название продукта: ")
new_product['price'] = int(input("Введите цену продукта: "))
new_product['weight'] = int(input("Введите вес продукта: "))
new_product['available'] = input("Товар в наличии? (Да/Нет): ").lower() == "да"

products.append(new_product)

with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

print("Обновленные данные:")
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
