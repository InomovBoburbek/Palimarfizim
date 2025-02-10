class Weapon:
    def __init__(self, name):
        self.name = name

    def use(self):
        print("paq - paq")


class Pistol(Weapon):
    def use(self):
        print(" Pistolet bilan o‘q otmoqdasiz!")


class Granad(Weapon):
    def use(self):
        print("Bom - Bom")


p = Pistol("A")
p.use()

g = Granad("B")

g.use()




# 22222 ikkinchi misol pastagisi




class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Bu hayvon ovoz chiqarmoqda!")


class Dog(Animal):
    def sound(self):
        print(" Vov - Vov")


class Cat(Animal):
    def sound(self):
        print(" Miyov - Miyov")


class Cow(Animal):
    def sound(self):
        print(" Mo‘ - Mo‘")


d = Dog("Rex")
d.sound()

c = Cat("Tom")
c.sound()

co = Cow("Burenka")
co.sound()




# 33333 misol bu pastagisi



class Vehicle:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Bu transport vositasi ovoz chiqarmoqda!")


class Car(Vehicle):
    def sound(self):
        print(" Vrum - Vrum")


class Motorcycle(Vehicle):
    def sound(self):
        print(" Brum - Brum")


class Truck(Vehicle):
    def sound(self):
        print(" Honk - Honk")


c = Car("BMW")
c.sound()

m = Motorcycle("Harley")
m.sound()

t = Truck("Volvo")
t.sound()




# 444444 misol pastdagi





class Clothing:
    def __init__(self, name):
        self.name = name

    def wear(self):
        print("Bu kiyim kiyilmoqda!")


class Shirt(Clothing):
    def wear(self):
        print(" Ko‘ylak kiyildi!")


class Pants(Clothing):
    def wear(self):
        print(" Shim kiyildi!")


class Jacket(Clothing):
    def wear(self):
        print(" Kurtka kiyildi!")


s = Shirt("T-shirt")
s.wear()

p = Pants("Jeans")
p.wear()

j = Jacket("Leather Jacket")
j.wear()



# 55555 misol pastdagi


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Salom, mening ismim {self.name}!")


class Doctor(Person):
    def introduce(self):
        print(f" Men doktor {self.name}, sizga yordam bera olaman!")


class Teacher(Person):
    def introduce(self):
        print(f" Men o‘qituvchi {self.name}, bilim ulashaman!")


class Engineer(Person):
    def introduce(self):
        print(f" Men muhandis {self.name}, loyihalar yarataman!")


d = Doctor("Akmal")
d.introduce()

t = Teacher("Laylo")
t.introduce()

e = Engineer("Javohir")
e.introduce()


