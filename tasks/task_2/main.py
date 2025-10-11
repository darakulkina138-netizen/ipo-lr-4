n = input("Введите числа через пробел: ").split()
n = [int(x) for x in n]
#Возведение в квадрат
s = [x**2 for x in n]
print(s)
