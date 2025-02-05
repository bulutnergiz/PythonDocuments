

x = 50
def test(x):
    print(f"ilk x değeri {x}")

    x = 100
    print(f"x in yeni değeri {x}") #burayı yorum satırı yaparsan üstteki x soluk gri oluyor. yani hiçbir
                                   #yerde kullanılmıyor diyor değişken. önemli ayraç anlaman için
test(x)
print(f"x değerinin global değeri {x}")

print("------------------------------------------------------------------")


# x = 50        #bu hali oynatınca hata veriyor çünkü text(x) yazıları içinde x olmamalı
# def test(x):    # alttaki hücrede doğru hali var
#     global x
#     print(f"x değeri {x}")
#
#     x = 100
#     print(f"x in yeni değeri {x}")
#
# test(x)
# print(x)


print("------------------------------------------------------------------")


x = 50
def test():
    global x   #global alınca artık fonk içindeki değişiklikler global değişken üzerinde oluyor
    print(f"ilk x değeri {x}")

    x = 100
    print(f"x in yeni değeri {x}")

test()
print(f"x değerinin global değeri {x}")


print("------------------------------------------------------------------")


