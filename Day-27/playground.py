# *args => Unlimited positional arguments, its type is tuple
# **kwargs => Unlimited keyword arguments, its type is dictionary

def add(*args):
    s=0
    for n in args:
        s += n
    return s

print(add(1,2,3,4,5))

def calculate(n, **kwargs):
    print(kwargs)

    for key, value in kwargs.items():
        print(key)
        print(value)

    print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

# kwargs.get("add") is equivalent to kwargs["add"] but with better error handling as it returns none when the given key
# is not found whereas kwargs["add"] will throw an error

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

my_car = Car(make="Tata", model="Altroz", color="Gray")
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)