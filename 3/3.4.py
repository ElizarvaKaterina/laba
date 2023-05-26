import random
correct_answers = 0
mistakes = 0
while mistakes < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    expression = str(a) + " + " + str(b) + " = "
    answer = input(expression)
    if int(answer) == a + b:
        print("Правильно!")
        correct_answers += 1
    else:
        print("Ответ неверный")
        mistakes += 1
print("Игра окончена. Правильных ответов:", correct_answers)
