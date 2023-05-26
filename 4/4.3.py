def z3():
    date = input('Введите дату в формате дд.мм.гггг: ')
    date = date.split('.')
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print('Дата магическая!')
    else:
        print('Дата не является магической')
