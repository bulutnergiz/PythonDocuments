#
print("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
#
#STRİNG FORMATLAMA - F STRİNGE BENZER BİR ARAÇ
name = "Mehmet"
surname = "Coni"
print("My name is {} {}".format(name, surname))
print("My name is {1} {0}".format(name, surname))
print("My name is {s} {n}".format(n=name, s=surname))
print("My name is {} {} and I am {} years old.".format(name, surname, "30"))
print("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
result = 2 / 7
print("Result is {}".format(result))
print("Result is {r:0.4}".format(r=result))
print("Result is {r:6.4}".format(r=result)) #sayı uzunluğu noktayla birlikte 6 oluyor
print("Result is {r:9.4}".format(r=result))
#0 kısmı kaç boşluk olacağı-sayının kendisi dahil uzunluğa, 4 ise virgülden sonra ne kadar alacağı
print(f"My {name} is you now this is easy and special tool for python")
#
print("222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222")
#
#STRİNG METOTLARI
s = "Hello world"
# s[6] = "W" böyle bi şey yok
s = s[0:6] + "W" + s[-4:]
print(s)
s = "Hello worldw"
s = s.replace("w","W")
print(s)
print("222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222")
message = "   Hello Coni I am Memo"
message = message.strip() #Strip sağ ve soldan boşlukları siler. lstrip soldan rstrip sağdan siler.
print(message)
message = "   Hello Coni I am Memo"
message = message.strip("HelCi ")
print(message)
message = "   Hello Coni I am Memo"
message = message.split()
print(message)
message = " ".join(message)
print(message)
print("33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333")
message = message.center(30, "*")
print(message)
message = message.rjust(30, "*")
message = message.ljust(30, "*")
#
print("33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333")
#
#LİSTELER
usera = ["Coni", 25]
userb = ["Lena", 30]
print(usera+userb)
users = [usera, userb]
print(users)
print(users[0][1]) # usera ya gidiyor ve onun 1.indexi yani 25 sayısına gidiyor
print("4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444")
numbers = [1,2,3,4,5]
numbers.insert(3, 55) #3.indexe 55 koy ve devamını kaydır.
print(numbers)

nums = [0,5,16,4,76,26]
nums.reverse() # büyükten küçüğe sıralı için önce sort sonra reverse atman gerek.
print(nums) #reverse olan hali ters çeviriyor. sort gibi büyükten küçüğe değil.
#nums.clear() listenin tüm elemanlarını siler içi boş bir liste verir.
print("4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444")



