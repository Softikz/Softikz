#Задание.Создайте класс героя,у которого будут обязательные характеристики
#здоровье выносливость    2 любых атаки __str__ - который будут показывать состояние обЪекта
import random


class hero:
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.manna=100
        self.lvl = 100
    def __str__(self):
        return f'Боец {self.name},\n Здоровье:{self.hp},\n Выносливость на момент:{self.manna}, \n Его узнаваемость и сила:{self.lvl}'
    def KO(self,target):
        if self.manna >=25:
             dmg = random.randint(20,50)
             print(f'{self.name} атаковал нокаутом с уроном {dmg}')
             target.hp -=dmg
             self.manna -= 25

        else:
            print('Вам нужно отдохнуть и набраться выносливости')

    def wait(self):
        print(f'{self.manna} отдохнул и востановил 20 выносливости')
        self.manna += 20
        if self.manna >=100:
            self.manna = 100
    def kick(self,target):
        if self.manna >=10:
            dmg = random.randint(10, 20)
            print(f'{self.name} атаковал ударом ногой с уроном{dmg}')
            target.hp -= dmg
            self.manna -= 10
        else:
            print('Вам нужно отдохнуть и набраться выносливости')

my_hero = hero("Конор Маггрегор")
smb = hero('Хасбик')
print(my_hero)
my_hero.KO(smb)
print(smb)
smb.kick(my_hero)
print(my_hero)
