a = int(input('Введите первую цифру: '))
b = int(input('Введите вторую цифру: '))
c = int(input('Введите третью цифру: '))
print((a * 100) + (b * 10) + c)


a = int(input('Введите число состоящие из 4 цифр: '))
b = (a - (a % 1000)) / 1000
b1 = a % 1000
c = (b1 - (b1 % 100)) / 100
c1 = b1 % 100
d = (c1 - (c1 % 10)) / 10
e = a % 10
print(b * c * d * e)


a = int(input('Введите количество метров: '))
bm = a * 100
cm = a * 10
dm = a * 1000
em = a * 0.000621371192
print(f"""Сантиметров: {bm}
Дециметров: {cm}
Миллиметров: {dm}
Миль: {em}""")


t1 = int(input('Введите размер основания треугольника: '))
t2 = int(input('Введите размер высоты треугольника: '))
t3 = 0.5 * t1 * t2
print('Площадь треугольника: ' + str(t3))


a = int(input('Введите число состоящие из 4 цифр: '))
b = (a - (a % 1000)) / 1000
b1 = a % 1000
c = (b1 - (b1 % 100)) / 100
c1 = b1 % 100
d = (c1 - (c1 % 10)) / 10
e = a % 10
print((e * 1000) + (d * 100) + (c * 10) + b)
