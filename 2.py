print('Введите длину первого катета:')
a = int(input())
print('Введите длину второго катета:')
b = int(input())
S = (a * b)/2
P = a + b + ((a*a) + (b*b))**(0.5)
print('Площадь прямоугольного треугольника = ', S, 'Периметр прямоугольного треугольника = ', P)