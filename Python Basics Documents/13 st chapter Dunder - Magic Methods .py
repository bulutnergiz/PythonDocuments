

class movie():
    def __init__(self, name, country, duration):
        movie.name = name
        movie.country = country
        movie.duration = duration
    def __str__(self):
        return f"{self.name}, {self.country} ülkesine ait. "
    def __len__(self):
        return self.duration
    def __del__(self):                #eğer obje silinirse siliyor ve ek olarak bunu çalıştırıyor o anda
        print("bu film kitaplıktan kaldırıldı(bu obje silindi)")

m = movie("Story of Lena", "France", 95)
print(m)
print(str(m)) # bu ve üstteki arasındaki farkı çözsen iyi olur.
print("*****")
print(len(m))

del m
# print(m) bunu yazınca m tanımlanmadı diyor



print("--------------------------------------------------------------------")




print(3+5)
print(int.__add__(3,5)) #dunder methods örnek
print("Ali" + "Veli")
print(str.__add__("Ali", "Veli"))
print([1, 2, 3] + [4, 5, 6])
print(list.__add__([1,2,3], [4,5,6]))




print("*******")



class Sadık_Liste(list): #normal liste üzerinde hiçbir değişiklik yapmadık. listeyi komple miras aldık.
    pass
sadıkEleman1 = Sadık_Liste([1,2])
sadıkEleman2 = Sadık_Liste([3,4])
print(sadıkEleman1 + sadıkEleman2)



class Sadık_Olmayan_Liste(list):
    def __add__(self, other):
        if  len(self) != len(other):
            return "Liste uzunklukları eşit değil, bu listeler toplanamaz. "
        else:
            result = Sadık_Olmayan_Liste() #boş bi liste açıyoruz :)
            for i in range(len(self)):
                result.append(self[i] + other[i])
        return result



    def __sub__(self, other): #burada override simgesi yok çünkü listelerde tanımlı çıkarma işlemi yok
        if  len(self) != len(other):
            return "Liste uzunklukları eşit değil, bu listeler çıkarılamaz. "
        else:
            result = Sadık_Olmayan_Liste()
            for i in range(len(self)):
                result.append(self[i] - other[i])
        return result

    def __eq__(self, other):
        if sum(self) == sum(other):
            return True
        return False


sadıkOlmayanEleman1 = Sadık_Olmayan_Liste([1,2])
sadıkOlmayanEleman2 = Sadık_Olmayan_Liste([3,4])
print(sadıkOlmayanEleman1 + sadıkOlmayanEleman2)
print(sadıkOlmayanEleman1 - sadıkOlmayanEleman2)



print("--------------------------------------------------")




print(sadıkOlmayanEleman1 == sadıkOlmayanEleman2)

sadıkOlmayanEleman1 = Sadık_Olmayan_Liste([1,2,4])
print(sadıkOlmayanEleman1)
print(sadıkOlmayanEleman2)
print(sadıkOlmayanEleman1 == sadıkOlmayanEleman2)


print("--------------------------------------------------")



class Futbolcu:
    def __init__(self, isim, soyisim, yaş):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş

    def __eq__(self, other): #iki futbolcunun adı soyadı aynı mı
        if self.isim == other.isim and self.soyisim == other.soyisim:
            return True
        return False

    def __add__(self, other):
        isim = self.isim[0] + other.isim[0]
        soyisim = self.soyisim[0] + other.soyisim[0]
        yaş = self.yaş + other.yaş
        return Futbolcu(isim, soyisim, yaş)


futbolcu1 = Futbolcu("Ali", "Veli", 27)
futbolcu2 = Futbolcu("Hakan", "Metin", 30)


print(futbolcu1 == futbolcu2)

futbolcu3 = futbolcu1 + futbolcu2
print(futbolcu3.isim)
print(futbolcu3.soyisim)
print(futbolcu3.yaş)
print(futbolcu3) #<__main__.Futbolcu object at 0x0000022CEDE46610> bunu yazdırmasın diye _str_ kullanıyoz
print(str(futbolcu3))

# def __str__(self):
#     return f"{self.name}, {self.country} ülkesine ait. " böyle bir şeyi metot olarak tanımlamamız lazım


print("--------------------------------------------------")



# str ve repr dunders

a = "python"
print(str(a))
print(repr(a))

a = 2/11
print(str(a))
print(repr(a))

from datetime import date
import datetime

bugün = date.today()
print(bugün)
print(str(bugün))  #son kullanıcının görmesini istediğimiz şeyler
print(repr(bugün))  #parametreler budur vs. şeklinde parametre fonks. biçiminde veriyor - yazılımcı kendi için
print(datetime.date(2023, 12, 3))




print("--------------------------------------------------")

# str ve repr dunders devam

class Futbolcu:
    def __init__(self, isim, soyisim, yaş):
        self. isim = isim
        self.soyisim = soyisim
        self.yaş = yaş

futbolcu1 = Futbolcu("Ali", "Veli", 25)
print(futbolcu1)  #<__main__.Futbolcu object at 0x000001D0B9B51210>       bunu yazdırır



class Futbolcu:
    def __init__(self, isim, soyisim, yaş):
        self. isim = isim
        self.soyisim = soyisim
        self.yaş = yaş

    def __str__(self):
        return (f"Ad: {self.isim}, Soyad: {self.soyisim}, Yaş: {self.yaş}")

    def __repr__(self):
        return f'Futbolcu("{self.isim}", {self.soyisim}, {self.yaş})'

futbolcu1 = Futbolcu("Ali", "Veli", 25)
print(futbolcu1) #printe özellikle repr demezsen str yi önceliklendirir - print(repr(futbolcu1))
                 # ayrıca eğer str olmazsa print repr 'a gider      veya- print(futbolcu1.__repr__())

print(repr(futbolcu1)) # bunu | futbolcux = Futbolcu("Ali", Veli, 25) | olarak yapıştırırsam nesne yaratılır


















