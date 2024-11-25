import random

class Animal: # класс описывающий животных.
    live = True
    sound = None #звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 #степень опасности существа
    def __init__(self, _cords, speed):
        self._cords = [0, 0, 0] #координаты в пространстве.
        self.speed = speed #скорость передвижения существа (определяется при создании объекта)

    def move(self, dx, dy, dz):
        self._cords[1] += dx * self.speed
        self._cords[2] += dy * self.speed
        self._cords[3] += dz * self.speed
        if self._cords[3] <= 0:
            print("It's too deep, i can't dive :(")
            self._cords[3] = 0

    def get_cords(self):
        print(f'X: {self._cords[1]}, Y:  {self._cords[2]}, Z:  {self._cords[3]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal): #Класс описывающий птиц. Наследуется от Animal.
    beak = True #наличие клюва

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")#который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"

class AquaticAnimal(Animal): #Класс описывающий плавающего животного. Наследуется от Animal.
    _DEGREE_OF_DANGER = 3
    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        self._cords[3] = -(abs(dz) * self.speed)/2

class PoisonousAnimal(Animal): #Класс описывающий ядовитых животных. Наследуется от Animal
    _DEGREE_OF_DANGER = 8

class Duckbill( AquaticAnimal, Bird, PoisonousAnimal): #класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
    def __init__(self, speed):
        super().__init__(speed)

    def speak(self, sound):
        super().sound()
        self.sound = "Click-click-click" # звук, который издаёт утконос
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
