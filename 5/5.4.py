a1 = ['Поляков', 'Рябов', 'Лазарев', 'Журавлёв']
a2 = ['Назаров', 'Елисеев', 'Кабанов', 'Маслов']
team = a1[0:3]+a2[2:4]
print('Первая группа', a1)
print('Вторая группа', a2)
print('Спортивная команда', team)
print("Длина кортежа", len(team))
team_sorted = sorted(team)
print("Отсортированный кортеж: ", team_sorted)
polacov_count = team.count("Поляков")
if polacov_count > 0:
    print("Фамилия Поляков встречается в команде ", polacov_count, " раз(а).")
else:
    print("Фамилия Поляков не входит в команду.")
