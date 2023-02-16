pas=input('Введите пароль')
if len(pas) < 6:
    print('Слишком короткий пароль')
elif pas[0:7]=="qwerty":
    print('Ненадежный пароль')

else:
    print('ok')