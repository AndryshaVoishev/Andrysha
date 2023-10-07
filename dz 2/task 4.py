stroka = input('Введите строку со скобками: ')
a = stroka.count('(')
b = stroka.count(')')

if a < b:
    print('Не хватает', b - a, 'открывающей скобки')
elif a > b:
    print('Не хватает', a - b, 'закрывающей скобки')
else:
    print('All right')
