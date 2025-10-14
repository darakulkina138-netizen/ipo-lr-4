#Автор darakulkina138-netizen
num = input("Введите числа через пробел: ")
num1 = [float(x) for x in num.split()]
square = [x**2 for x in num1]
print(square)
