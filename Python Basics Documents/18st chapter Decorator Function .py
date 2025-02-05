

# Decorator Fonk

def my_decorator(func):
    def wrapper():
        print("fonksiyondan önceki işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    return wrapper

def sayHello():
    print("hello")

sayHello = my_decorator(sayHello)

sayHello()

print("\n*******************\n")


def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önceki işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper


@my_decorator
def alternatifYol(name):
    print("alternatif hello " + name)

alternatifYol("Lena")




print("\n------------------------------------------------------------------------\n")



#pratik olarak gerçekte nerede kullanacağımıza örnek

import math
import time


"""
her fonksiyona tek tek süre ölçme eklemek yerine decorator kullanıyoruz aşağıdaki gibi

def üsalma(a,b):
    start = time.time()
    time.sleep(1)

    print(math.pow(a,b))

    finish = time.time()
    print("fonksiyon " + str(finish-start) + " saniye sürdü. ")

def faktoriyel(a):
    start = time.time()
    time.sleep(1)

    print(math.factorial(a))

    finish = time.time()
    print("fonksiyon " + str(finish-start) + " saniye sürdü. ")

üsalma(3,4)
faktoriyel(5)

"""





#şu kullanımda ustalaşman lazım
def calculateTime(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon " + func.__name__ + " " + str(finish - start) + " saniye sürdü. ")
    return inner



@calculateTime
def üsalma(a,b):
    print(math.pow(a,b))


@calculateTime
def faktoriyel(a):
    print(math.factorial(a))




üsalma(3,4)
faktoriyel(5)

print("\n*******************\n") #aşağıdaki ve yukarıdaki kullanım arasında fark yok

calculateTime(üsalma(3,4))
calculateTime(faktoriyel(5))

#yani artık istersen yarattığın fonksiyonu direkt kullan istersen süresini ölçtüğün bir fonka çevirirsin




















