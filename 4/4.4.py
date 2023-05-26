try:
    ticket = input("Введите номер билета: ")
    k = 0
    k1 = 0
    l1 = ticket[0:int(len(ticket)/2)]
    l2 = ticket[int(len(ticket)/2):int(len(ticket))+1]
    if len(ticket) % 2 == 0:
        for i in l1:
            k = k+int(i)
        for i in l2:
            k1 = k1+int(i)
        if k == k1:
            print("Билет", ticket, "счастливый!")
        else:
            print("Билет не счастливый")
    else:
        print("Количество цифр должно быть нечетно.")
except ValueError:
    print("Введите только числа")
