# print("hello world")

name="nadia"
last_name="nguyen"

# print("Hello {} {}".format(name,last_name))

# print(f'Hellp there {name} {last_name}')

if (name=="nadia"):
    pass
    # print("cool")
elif name=="patricia":
    print("very cool")
else:
    print("okay")

x = "cool"
x = True
x = 4
x = 1.4

print(x)

w = {
    # Key                 value
    "favorite_food" : "spagetti",
    "favorite_number" : 7,
    "loves_python" : True
}

w["favorite_food"] = "burrargljaerkl"
# print(w["favorite_food"])

# for key in w:
#     print(f"{key} , {w[key]}")

# for key, value in w.items():
#     print(f"{key} , {value}")

t = [1,4,6456,234,457,134]


#              start, end, jump
for i in range(0,len(t),1):
    print(t[i])

# for i in range(len(t)):
#     print(t[i])

class Person:
    first_name = ""
    last_name = ""

# constructor
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
    
#  Function
    def print_person(self):
        print(f"{self.first_name} {self.last_name}")


henry = Person("Henry", "Le")
kaye = Person("Kaye", "K")

henry.print_person()
