# Object Oriented Programming - OOP


print("-----------------------------------------------------------------------------")

#bir taslak

class person:
        # class object attributes
        address = "belirtilmemiş"
        # constructor(yapıcı metod)
        def __init__(self, name, year):
            #object attributes
            self.name = name
            self.year = year

        # methods

#instance(object)


print("-----------------------------------------------------------------------------")


class person:
    # class object attributes
    address = "belirtilmemiş"
    # constructor(yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year

    # methods
    # instance method örneği
    def starting(self):
        print(f"Hoş geldin {self.name}")

    # instance method örneği
    def calculate_age(self):
        return 2024 - self.year



user1 = person("Lena", 1995)
user1.starting()
print(user1.calculate_age())



print("-----------------------------------------------------------------------------")



class circle:
    # class object attribute
    pi = 3.14
    # constructor(yapıcı metod)
    def __init__(self, yaricap = 1): # fonksiyonda varsayılan değer kullanımı
        #object attributes
        self.deneme = yaricap
    #methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.deneme #self.yaricap = yaricap yaparız burada da self.yaricap olur
    def alan_hesapla(self):
        return self.pi * ((self.deneme) ** 2)
        # print(self.pi * ((self.Modüler çalışma denemesi) ** 2)) ##böyle print olursa alınan hatayı gözden kaçırma

c1 = circle()
c2 = circle(3)
print(f"c1 dairesinin çevresi {c1.cevre_hesapla()} ve alanı {c1.alan_hesapla()}")
print(f"c2 dairesinin çevresi {c2.cevre_hesapla()} ve alanı {c2.alan_hesapla()}")

print(c1.pi)
