from PIL import Image, ImageDraw, ImageFont

greetings = {"Новый год": "new_year.jpg", "День рождения": "bithday.jpg", "День Святого Валентина": "valentine.jpg"}
holiday = input("Введите название праздника: ")
if holiday in greetings:
    image = Image.open(greetings[holiday])
    name = input("Введите имя человека, которого хотите поздравить: ")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 60)
    text = f"{name}, поздравляю!"
    text_windth, text_height = draw.textsize(text, font)
    x = (image.width - text_windth) / 2
    y = image.height - text_height - 50
    draw.text((x, y), text, font=font, fill=(255, 0, 0, 255))
    image.show()
    image.save("greeting.jpg")
else:
    print("Открытки для такого праздника нет")
