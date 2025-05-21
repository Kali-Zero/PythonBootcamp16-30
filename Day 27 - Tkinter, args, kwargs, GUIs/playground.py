#Unlimited Positional Arguments (Order can matter)
def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum

#print(add(1,2,3,5,6,7,8,9,))

#Works as Dictionary
def calculate(n, **kwargs):  #KWARD = Key Word Argument
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']

    #print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        #.get is better, because it won't immediately break if there is no value attached.
        self.make = kw.get('make')
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make='Ford', model='Escort')
print(my_car.make)
print(my_car.model)
print(my_car.color)