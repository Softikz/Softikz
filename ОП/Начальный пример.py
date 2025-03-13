
class Car:
    def __init__(self, mark, color):
        self.mark = mark
        self.color = color
        self.speed = 0
    def __str__(self):
        return f' Машина марки {self.mark},цвета {self.color},скорость {self.speed}'
    def gas(self, s):
        self.speed += s
    def break_car(self):
        self.speed = 0

black_car = Car('Bugatti','black')
red_car = Car('Veyron','red')


print(black_car)
black_car.gas(10)
print(black_car)
black_car.break_car()
print(black_car)
