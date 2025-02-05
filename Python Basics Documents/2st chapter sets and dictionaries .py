
students = {}
number = input("Enter your number: ")
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
phone = input("Enter your phone: ")
number2 = input("Enter your number: ")
name2 = input("Enter your name: ")
surname2 = input("Enter your surname: ")
age2 = input("Enter your age: ")
phone2 = input("Enter your phone: ")

# students.update({number: {"name": name}})   BİÇİM BU ASLINDA
students.update({
    number: {
        "ad": name,
        "soyad": surname,
        "yaş": age,
        "numara": phone
    },
    number2: {
        "ad": name2,
        "soyad": surname2,
        "yaş": age2,
        "numara": phone2
    }
})

print(students)


print("------------------------------------------------------------------")


find_this_student = input("Bulmak istediğin öğrencinin numarası nedir?: ")
print(f"{find_this_student} numaralı öğrencinin adı {students[find_this_student]['ad']}")
# print(f"{find_this_student} numaralı öğrencinin adı {students[find_this_student['ad']]}") - HATALI
# print(students["002"]["ad"]) - DOĞRU KULLANIM


print("------------------------------------------------------------------")

#sete ekleme için add ve uptade kullanılabilir
#sette silme için remove, discard kullanılabilir(parametre eleman). pop ile rastgele eleman siler
#clear da her şeyi siler aynı şekilde
setim = {"apple", "banana"}
setim.add("cherry")
print(setim)
listem = [1,2,3,4,5,1,2,3]
print(set(listem))


