
from PIL import Image

greetings = {"Новый год": "new_year.jpg", "День рождения": "birthday.jpg", "День Святого Валентина": "valentine.jpg"}
holiday = input("Введите название праздника: ")
if holiday in greetings:
    image = Image.open(greetings[holiday])
    image.show()
else:
    print("Открытки для такого праздника нет")
