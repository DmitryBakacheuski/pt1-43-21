'''Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы и условные операторы.
 n - вводится
'''
n = int(input())
a = 1
d = 0
b = 1
while a != n :
    c = d + b
    a += 1
    b = d
    d = c
print(c)
