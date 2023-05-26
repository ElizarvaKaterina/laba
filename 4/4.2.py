try:
    a = int(input('Введите число: '))
    b = 100 / a
except ValueError:
    print("Введите только числа")
except ZeroDivisionError:
    print('Введен 0!')
else:
    print('Результат от деления 100 на введенное число ', b)
