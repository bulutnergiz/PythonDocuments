# Inheritance (Kalıtım) : Miras alma

#Person classı => name - lastname - age bilgilerine ve eat() - drink() - run() metotlarına sahip.
#Student(Person) classı da Person özelliklerini taşıyor, ayrıca öğrenciye has eklemelere sahip
#Teacher(Person) classı da Person özelliklerini taşıyor, ayrıca öğretmene has eklemelere sahip

#Animal classı => ...
#Dog(Animal) classı Animal özelliklerini taşıyor, ayrıca köpeklere has bazı eklemelere sahip
#Cat(Animal) classı Animal özelliklerini taşıyor, ayrıca kedilere has bazı eklemelere sahip



print("----------------------------------------------------------------------------")


class animal():
    def __init__(self, color):
        self.color = color
        print("animal classındaki her şeye sahip")
    def deneme_metot(self):
        print("animal classındaki metot çalıştı")


class dog(animal):
    def __init__(self, color):
        animal.__init__(self, color)
        print("dog yaratıldı")

p1 = animal("white") # a white bear
print("******")
d1 = dog("black")
print("******")
print(f"Hayvanın rengi {p1.color}")
print(f"Köpeğin rengi {d1.color}") # dog classında self.color = color gibi ifade yok, persondan alıyor

print("----------------------------------------------------------------------------")



class animal():
    def __init__(self, color):
        self.color = color
        print("animal classındaki her şeye sahip")
    def deneme_metot(self):
        print("animal classındaki metot çalıştı")


class dog(animal):
    def __init__(self, color):
        animal.__init__(self, color)
        print("dog yaratıldı")

p1 = animal("white") # a white bear
print("******")
d1 = dog("black")

print("******")
p1.deneme_metot()
d1.deneme_metot() #animal classı içerisinden ulaşıyor buna, dog classında böyle bi metot yok



print("----------------------------------------------------------------------------")



class animal():
    def __init__(self, color):
        self.color = color
        print("animal classındaki her şeye sahip")
    def deneme_metot(self):
        print("animal classındaki metot çalıştı")


class dog(animal):
    def __init__(self, color):
        animal.__init__(self, color)
        print("dog yaratıldı")

    def deneme_metot(self): #burada açılan aynı isimli metot temel sınıftaki metodu ezer - override
        print("dog içindeki metot çalıştı, temel sınıftaki metodu ezdik - override")


p1 = animal("white") # a white bear
print("******")
d1 = dog("black")

print("******")
p1.deneme_metot()
d1.deneme_metot()



print("----------------------------------------------------------------------------")

#içerideki class'a özgü özellik eklenmesi

class animal():
    def __init__(self, color, name):
        self.color = color
        self.name = name

class dog(animal):
    def __init__(self, color, name, special_name):
        animal.__init__(self, color, name) # super().__init__(color, name) #BU İKİSİ AYNI ŞEY. BİL.
        self.special_name = special_name


p1 = animal("white", "bear") # a white bear
d1 = dog("black", "dog", "Karabaş")

print(p1.color, p1.name)
print(d1.color, d1.name, d1.special_name)


print("----------------------------------------------------------------------------")

#yeni bir class açma ve minik bir özellik

class cat(animal):
    def __init__(self, color, name, special_name):
        super().__init__(color, name) #animal.__init__(self, color, name) ile bu aynı şey
        self.special_name = special_name
    def kediye_özgü(self):
        print("kediler sınıfına özgü")

cat1 = cat("gray", "cat", "duman")
print(cat1.color, cat1.name, cat1.special_name)
cat1.kediye_özgü()



