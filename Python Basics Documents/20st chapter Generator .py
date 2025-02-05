

# Generators


def cube():
    result = []
    for i in range(5):
        result.append(i ** 3)
    return result
print(cube())
#burada result listesinde veriler tutuluyor yani bellekte veri kaplıyor. x 5 bin olursa gereksiz bellek kullanımı

print("---")

def cube():
    for i in range(5):
        yield i ** 3

küpler = cube()
print(küpler) #cube fonkunu çalıştırınca bize iterable bir obje veriyor. yani:
              # küpler objesi bir iterable obje(yani generator) , [0, 1, 8, 27, 64] böyle bir liste değil


print("---")


def cube():
    for i in range(5):
        yield i ** 3

generator = cube()

iteratör = iter(generator) #generator denen iterable objeyi iter fonk.u ile iteratöre atadık.

# print(next(iteratör))
# print(next(iteratör))
# print(next(iteratör))


while True:
    try:
        print(next(iteratör))
    except StopIteration:
        break



print("------------------------")

# generator = cube()
#
# iteratör = iter(generator) #yorum satırı olan yer ve alttaki yorum satırı kısım açılınca çalışıyorlar

for i in iteratör:
    print(i)

print("***")

# generator = cube()
#
# iteratör = iter(generator)

#en pratik ve bizim sürekli kullandığımız bu. Çünkü stop iteration hatasıyla uğraşmıyoruz
for i in generator:
    print(i)

print("------------------------")






def cube():
    for i in range(5):
        yield i ** 3

generator = cube()
print("ilk parçadayız")
print(next(generator))
print(next(generator))


iteratör = iter(generator)
print("ikinci parçadayız")
print(next(iteratör))


#generator ün kendisi de iterable obje. onu iter ile başka bir objeye de atayabiliriz. genelde direkt
#kendisini kullanırız. kritik nokta şu, bu iterale objede bir kere ilerleyince artık geri dönüş yok.
# dolayısı ile bi kere print next basınca artık farklı şekilde çağırsan da baştan başlamaz.
#üstteki iki farklı biçim bi kenara aşağıdaki gibi çağırsan dahi iş değişmiyor.
print("üçüncü parçadayız")
while True:
    try:
        print(next(iteratör))
    except StopIteration:
        break




#Tüm konu anlatımı sonrasında günlük kullanım şeklini gösterelim:

print("------------------------final hali")
def cube():
    for i in range(5):
        yield i ** 3

for i in cube():
    print(i)






# Generator sadece fonk.ta değil comphrension'da da kullanılır
print("------------------------")
liste = [x for x in range(5)] #liste döndürür
print(liste)
generator = (x for x in range(5)) #liste değil generator döndürür
print(generator)
for i in generator:
    print(i)


