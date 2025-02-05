#while için bir not
name = "" #WOW this is unbelievable
while name == "":
    name = input("İsim giriniz: ").strip()


print("------------------------------------------------------------------")


#döngüye dair birkaç not - enumerate
mesaj = "Helo"
for item in enumerate(mesaj):
    print(item)

for index, item in enumerate(mesaj):
    print(f"indeximiz: {index}, harfimiz: {item}")


print("------------------------------------------------------------------")


#döngüye dair birkaç not - zip metodu
list1 = [1,2,3,4]
list2 = ["a", "b", "c"]
list3 = list(zip(list1, list2))
print(list3)

for element in list3:
    print(element)

for x, y in list3:
    print(f"sayı: {x}, sayıya karşılık gelen harf: {y}")

list0 = ["m","n"]
list1 = [1,2,3,4]
list2 = ["a", "b", "c"]
list3 = list(zip(list1, list2,list0))
print(list3)

print("------------------------------------------------------------------")


#AŞIRI ÖNEMLİ
#stringin harflerini listye yapma, pratik şekilde for a in ... şeklinde ifade ile ekleme vs yapma
numbers = [x**2 for x in range(5)]
print(numbers)

word = "kelime"
numlist = [i for i in word]
print(numlist)

numbers = [x**2 for x in range(5) if x != 2]
print(numbers)

print("------------------------------------------------------------------")

result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))
print(result)

result2 = [(x, y) for x in range(3) for y in range(3)]
print(result2)

