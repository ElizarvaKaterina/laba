result = ""
while True:
    word = input("Введите слово: ")
    if word == "stop":
        break
    result += word + " "
if "ф" in result:
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")
