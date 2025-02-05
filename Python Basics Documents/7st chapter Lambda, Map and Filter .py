



numbers = [1,2,3,4,5,6]
def checkeven(num): return num % 2 == 0             #def checkeven(num):  #bu kullanımı soldaki gibi de
                                                        #return num % 2 == 0 # yazabiliyoz tek satırda

result = list(map(checkeven, numbers))
print(result)
result2 = list(filter(checkeven, numbers))   #map ve filter farkı bu
print(result2)


print("------------------------------------------------------------------")


result = list(map(lambda num: num % 2 == 0, numbers))  #map ve filter farkı lambda ile
print(result)
result2 = list(filter(lambda num: num % 2 == 0, numbers))
print(result2)


print("------------------------------------------------------------------")


checkevenX = lambda num: num % 2 == 0
result = list(map(checkevenX, numbers))
print(result)
checkevenX = lambda num: num % 2 == 0
result2 = list(filter(checkevenX, numbers))
print(result2)


print("------------------------------------------------------------------")


