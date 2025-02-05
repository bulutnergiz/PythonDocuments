#bir lsitedeki sadece sayıları döndüren öbür türlü value error veren bi try
#q basınca çıkış. sayı girmediyse value error sayı girdiyse sayıyıy döndüren bi döngü. sayı alana dek ddöngü.
#parola türkçe karakter içeriyorsa o zaman parola türkçe karakter içeremez hatası. Type error
#faktoriyel fonk. eğer negatif sayı ya da harfli bi şey girerse hata döndür.







liste = ["1", "2", "2a", "60x", "50"]

for x in liste:
    try:
        result = int(x)
        print(x)
    except ValueError:
        continue




print("----------------------------------------------------------------")



#q basınca çıkış. bir sayı girene dek sayı girmeni isteyen bir döngü

while True:
    sayı = input("Sayı gir: ")
    if sayı == "q":
        break

    try:
        result = int(sayı)
        break
    except ValueError:
        print("Bu bir sayı değil. ")
        continue






print("----------------------------------------------------------------")





def check(psw):
    türkçeKarakterler = "şçğüöıİ"

    for i in parola:
        if i in türkçeKarakterler:
            raise TypeError("Paarola türkçe karakter içeremez. ")
        else:
            pass

    print(f"geçerli parola: {parola} ")


parola = input("Parola gir: ")


try:
    (check(parola))
except TypeError as er:
    print(er)


# # kendi yaptığım
# def check(psw):
#     türkçeKarakterler = "şğöüİı"
#     for i in türkçeKarakterler:
#         print(i)
#         if i in psw:
#             raise TypeError("Parola Türkçe karakter içeremez. ")
#         else:
#             continue
#     return f"Şifreniz {psw} olarak belirlendi. "
#
# # print(check("mehmetğ"))
#
# try:
#     print(check("mehmetğ"))
# except TypeError as er:
#     print(er)


print("----------------------------------------------------------------")



def fakt(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif değerin faktoriyeli hesaplanamaz. ")

    result = 1
    for i in range(1, x+1):
        result *= i
    return result


for x in [5, 10, 20, -3, "1a"]:
    try:
        y = fakt(x)
    except ValueError as er:
        print(er)
        continue

    print(y)




print("------------------------------------------------------------------------------------------")



from math import factorial
def fakt(n):

    if type(n) != int:
        raise TypeError("Bir sayı girmeniz gerekiyor. ")
    elif n < 0:
        raise ValueError("Girdiğiniz sayı pozitif değil. ")
    elif n >= 0:
        return factorial(n)

a = -1

try:
    print(fakt(a))
except TypeError as er:
    print(er)
except ValueError as er:
    print("Negatif bir sayının faktoriyeli hesaplanamaz. ") #burası raise error kısmındakini eziyor
