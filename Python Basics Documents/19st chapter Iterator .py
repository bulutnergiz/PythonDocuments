

#Iterators


liste = [1,2,3,4,5]
for i in liste:
    print(i)

print("\n*******************\n")

#bunun yerne iteratorü yani iterable objeyi kendimiz yaratalım

iteratör = iter(liste)
print(next(iteratör))
print(next(iteratör))
print(next(iteratör))

print("\n------------------------------------------------------------------------\n")

#şimdi for döngüsünü kendi elimizle yazalım

iteratör = iter(liste)

while True:
    try:
        element = next(iteratör)
        print(element)
    except StopIteration:
        break




print("\n------------------------------------------------------------------------\n")



#kendi classımızı yaratınca tıpkı listetler gibi iterable objeler yaratmak isteyebiliriz
class MyNumbers:
    def __init__(self,start , stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration


#yol 1
list = MyNumbers(10,20)
for i in list:
    print(i, end=", ")

print("\n\n*****\n")

#yol 2
liste = MyNumbers(20,30)
iterableListe = iter(liste)

while True:
    try:
        print(next(iterableListe), end=", ")
    except StopIteration:
        break








