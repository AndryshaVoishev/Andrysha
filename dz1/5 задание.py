x = int(input('Введите координату для x: '))
y = int(input('Введите координату для y: '))
if x > 0 and y > 0:
    print('1 четверть')
elif x < 0 and y > 0:
    print('2 четверть')
elif x < 0 and y < 0:
    print('3 четверть')
elif x > 0 and y < 0:
    print('4 четверть')
elif x == 0 or y == 0:
    print('Точка лежит на оси')