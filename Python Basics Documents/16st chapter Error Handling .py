#Error Handling



# try:
#     x = int(input("Sayı 1: "))
#     y = int(input("Sayı 2: "))
#     print(x/y)

# except ZeroDivisionError:
#     print("Bir sayı sıfıra bölünemez! ")
#
# except ValueError:
#     print("Sayısal değer girmelisin! ")
#
# except (ValueError,ZeroDivisionError):
#     print("Yanlış bir bilgi girdiniz. Tekrar deneyin. ")

# except ValueError or ZeroDivisionError:
#     print("Yanlış bir bilgi girdiniz. Tekrar deneyin. ")
#
# except (ValueError,ZeroDivisionError) as e:
#     print(e)
#     print(f"{e} diye bir sayı yok. ") # sıfır girerse var aslında. yanlış bi örnek



# try:
#     x = int(input("Sayı 1: "))
#     y = int(input("Sayı 2: "))
#     print(x/y)
# except:       #Böyle de çalışır lakin burada ''as e'' gibi ifade alamayız çünkü hata türünü tutamaz bu form.
#     print("Yanlış bir bilgi girdiniz. Tekrar deneyin. ") # her türlü hata için çalışır, her türlü.


# while True:
#     try:
#         x = int(input("Sayı 1: "))
#         y = int(input("Sayı 2: "))
#         print(x/y)
#     except:
#         print("Yanlış bir bilgi girdiniz. Tekrar deneyin. ")
#     else:
#         # print("Her şey yolunda. ")
#         break



# while True:
#     try:
#         x = int(input("Sayı 1: "))
#         y = int(input("Sayı 2: "))
#         print(x/y)
#     except Exception as ex: #Zerodiverror syntax error value error vs hepsi bu Exception base clasına ait
#         print("Yanlış bir bilgi girdiniz. Tekrar deneyin. ", ex)
#     else:
#         # print("Her şey yolunda. ")
#         break
#     finally:
#         print("try except sonlandı. ")



# x = 10
# if x >= 5:
#     raise Exception("x 5'ten büyük olamaz. ")





class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("name alanı en fazla 10 karakterden oluşabilir. ")
        else:
            self.name = name

        self.year = year

şahıs1 = Person("Conconconi",1999)







def check_pasw(psw):
    import re
    if len(psw) < 8:
        raise Exception("Parola en az 8 karakterden oluşmalıdır. ")
    elif not re.search("[a-z]", psw):
        raise Exception("Parola en az bir tane küçük harf içermelidir. ")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola en az bir tane büyük harf içermelidir. ")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola en az bir tane rakam içermelidir. ")
    elif not re.search("[_.,:;!'^%+*/#${}()]", psw):
        raise Exception("Parola en az bir tane özel karakter içermelidir. ")
    elif re.search("\s", psw):
        raise Exception("Parola boşluk içermemelidir. ")
    else:
        print("Hata yok, geçerli parola")


parola = ("12")
try:
    check_pasw(parola)
except Exception as ex:
    print(ex)
else:
    print("Parolanız onaylandı, giriş ekranına yönlendiriliyorsunuz. ")
finally: #daima karşımıza çıkıyor doğru yanlış veya birinci ellinci iterasyon (döngü içinde) fark etmez.
    print("validation tamamlandı")

print("----------------------------------------------------------------------------------------------")

# # Assertion error muhabbeti de var şimdilik geçtik çünkü onu hiç kullanmadan da tüm işimizi görmüştük
# number = 42
# assert number > 0, f"number greater than 0 expected, got: {number}"
#
# number = -42
# assert number > 0, f"number greater than 0 expected, got: {number}"
#
#
# #bu daha güzel bi örnek
# # initializing number
# a = 4
# b = 0
#
# # using assert to check for 0
# print("The value of a / b is : ")
# assert b != 0, "b can't be zero"
# print(a / b)


# Assertion error muhabbeti de var şimdilik geçtik çünkü onu hiç kullanmadan da tüm işimizi görmüştük
number = 42
assert number > 0, f"number greater than 0 expected, got: {number}"

number = -42
assert number > 0, f"number greater than 0 expected, got: {number}"


#bu daha güzel bi örnek
# initializing number
a = 4
b = 0

# using assert to check for 0
print("The value of a / b is : ")
assert b != 0, "b can't be zero"
print(a / b)
