# Object Oriented Programming - OOP

#class
#instance (object)
list1 = [1,2,3] #list1, list class'ının içindeki bir objedir(instance).
print(type(list1))


# class person:
#     pass

print("-----------------------------------------------------------------------------")


#class x:
        #attributes (2 ye ayrılır)
        #1 - class attributes

        #--------------------------------------------------------------------------------------------
        #constructor(yapıcı metod) - object attributes bir constructer içinde tanımlanır
        #def __init__(self, name, year):      (constructor tanımlaması böyle yapılır - init metodu ile)
            #2 - object attributes
            #self.name = name
            #self.year = year
        # --------------------------------------------------------------------------------------------
        #methods

#instance(object)


class person:
    pass

p1 = person()
p2 = person()
print(p1)
print(p2)
print(type(p1))
print(type(p2))


print("-----------------------------------------------------------------------------")


class person:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print("init metodu çalıştı ")
# user1 = person() bunu yazıp durarak alacağı parametreler kısmını gözlemleyebilirsin
user1 = person("Lena", 25)
# user1 = person(name= "Lena", year= 25) - bu şekilde belirtirsen daha okunaklı olur
# user1 = person(year= "Lena", name= 25) - belirtirsen sırası önemsiz atadığın değere gider
print(user1)
#print(user1.) - bunu yazdıktan sonra tıpkı bir list.apppend vs çıkar gibi seçenekler çıkıyor. gözlemle
print(user1.name)
print(user1.year)
print(f"Kullanıcının ismi {user1.name} ve {user1.year} yaşında. ") # accesing object attributes


print("-----------------------------------------------------------------------------")

# class attributes - her zaman kullanılamyacak özellikler
# object attributes - obje tanımlandığı anda tanımlanmasını isteyeceğimiz özellikler
#Class attribute eklenmiş örnek
class person:
    address = "belirtilmemiş" # bir constructor içinde object attributes yerine dışarıda bir
    def __init__(self, name, year):  # class attribute açtık. 'address' bir class attribute.
        self.name = name             # class attribute, genel bir şey tanımlayacaksak kullanışlı gibi.
        self.year = year
        print("init metodu çalıştı ")
# user1 = person() bunu yazıp durarak alacağı parametreler kısmını gözlemleyebilirsin
user1 = person("Lena", 25)
# user1 = person(name= "Lena", year= 25) - bu şekilde belirtirsen daha okunaklı olur
# user1 = person(year= "Lena", name= 25) - belirtirsen sırası önemsiz atadığın değere gider
print(user1)
#print(user1.) - bunu yazdıktan sonra tıpkı bir list.apppend vs çıkar gibi seçenekler çıkıyor. gözlemle
print(user1.name)
print(user1.year)
print(f"Kullanıcının ismi {user1.name} ve {user1.year} yaşında. Adresi ise {user1.address}. ")


print("-----------------------------------------------------------------------------")


# updating örneği - değişiklikler yapılabilir
user1.name = "Lara" #adını değiştiğini düşünelim
user1.address = "Germany, Munchen" #yaşadığı yeri ise sisteme girmeye karar vermiş
print(user1)
print(f"Kullanıcının ismi {user1.name} ve {user1.year} yaşında. Adresi ise {user1.address}. ")

