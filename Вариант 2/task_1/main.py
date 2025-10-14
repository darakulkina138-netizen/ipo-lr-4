#Автор darakulkina138-netizen
num = int(input("Введите число для расчета факториала: "))
fact = 1
i = 1
while i <= num:
    fact *= i 
    i += 1
print(f"Факториал числа {num} равен {fact}")
