# Inheritance (Kalıtım) : Miras alma

#Person classı => name - lastname - age bilgilerine ve eat() - drink() - run() metotlarına sahip.
#Student(Person) classı da Person özelliklerini taşıyor, ayrıca öğrenciye has eklemelere sahip
#Teacher(Person) classı da Person özelliklerini taşıyor, ayrıca öğretmene has eklemelere sahip

#Animal classı => ...
#Dog(Animal) classı Animal özelliklerini taşıyor, ayrıca köpeklere has bazı eklemelere sahip
#Cat(Animal) classı Animal özelliklerini taşıyor, ayrıca kedilere has bazı eklemelere sahip



class animal():
    def __init__(self):
        print("animal classındaki her şeye sahip")

class dog(animal):
    pass

p1 = animal()
print("******")
s1 = dog()



print("----------------------------------------------------------------------------")


class animal():
    def __init__(self):
        print("animal classındaki her şeye sahip")

class dog(animal):
    def __init__(self):  #dog'un initi animal'ın initini eziyor - OVER RIDE
        print("dog yaratıldı") # sonraki hücrede bunu nasıl düzeltiriz gösteriyorum

p1 = animal()
print("******")
s1 = dog()


print("----------------------------------------------------------------------------")


class animal():
    def __init__(self):
        print("animal classındaki her şeye sahip")

class dog(animal):
    def __init__(self):
        animal.__init__(self)
        print("dog yaratıldı")

p1 = animal()
print("******")
s1 = dog()



print("----------------------------------------------------------------------------")









