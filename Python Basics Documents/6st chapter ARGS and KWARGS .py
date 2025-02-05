
def hello(name = "Lena"): #Fonksiyona varsayılan parametre ekleme
    print(f"Hello {name}. ")
hello()
hello("Coni")

print("------------------------------------------------------------------")


def addition(*all_elements):
    return sum(all_elements)
print(addition(1,2,3,4,5))


print("------------------------------------------------------------------")


# def user_info(**info): # iki ** olduğunda dictionary girdisi alacağını gösterir
#     for key, value in info.items(): # 4st chapter içinde bu durumun mnatığı var
#         print(f"{key} is {value}")
#
# #Buraları komple beceremedin - KWARGS
# user_info({"mehmet": 24, "ben": 21 })
# # user_info({"mehmet": 24, "ben": 21 })
# # one = {"name": "coni", "age": 24}
# # two = {"name": "lena", "age": 25, "mail": "lena@gmail.com"}
# one = (name= "coni", age: 24)
# two = (name = "lena", age = 25, mail = "lena@gmail.com")
# user_info(one)
# user_info(two)

def user_info(**info): # iki ** olduğunda dictionary girdisi alacağını gösterir
    for key, value in info.items(): # 4st chapter içinde bu durumun mnatığı var
        print(f"{key} is {value}")
    print(info)
user_info(name= "coni", age= 24) #bu ve önceki 4 satır çalışan bir kod örneği

# one = (name= "coni", age= 24)
# user_info(one)

