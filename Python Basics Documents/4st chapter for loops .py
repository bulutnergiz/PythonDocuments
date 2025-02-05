
dict1 = {"k1": 1, "k2": 2}
for i in dict1:
    print(i) # sadece key'leri yazdırır
print("------------------------------------------------------------------")
for i in dict1.items():
    print(i) #key ve value değerlerini bir tuple olarak almak için .items kullanırız
print("------------------------------------------------------------------")
for key, value in dict1.items():
    print(key)
print("------------------------------------------------------------------")
for key, value in dict1.items():
    print(value)

