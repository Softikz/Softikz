a = int(input("Введите начало последовательности (a): "))
b = int(input("Введите конец последовательности (b): "))
count = 0  # Счетчик кол-ва
summ = 0  # Сумма чисел
umnojenie = 1  # Произведение чисел
for i in range(a, b + 1):
    count += 1
    summ += i
    umnojenie *= i
print(f"Количество чисел в последовательности: {count}")
print(f"Сумма чисел: {summ}")
print(f"Произведение чисел: {umnojenie}")