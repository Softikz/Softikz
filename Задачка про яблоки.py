n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))
applesforchild = k // n
ostatok = k % n
print("Каждому школьнику достанется",applesforchild,"яблок.")
print("В корзинке останется",ostatok, "яблок.")