import time
def countdown(t):
    while t:
        mins,secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        print(t)
    print('Время вышло!')
# Введите время в минутах
t = int(input("Введите время для отсчета (в минутах): ")) * 60
countdown(t)
# Переводим минуты в секунды