try:
    a = int(input('Введите число, чтобы проверить деление на 3: '))
    b = a % 3
except ValueError:
    print('Введено не число!')
else:
    if b == 0 and a != 0:
        print('Число', a, 'делиться на 3!')
    elif a ==0:
        print('Введен ноль!')
    else:
        print('Число', a, 'не делиться на 3!')
