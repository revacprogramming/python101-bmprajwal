

class Menu(dict):
    def __setitem__(self, key = " ", value = 0):
        self.__dict__[key] = value

class Order(dict):
    def __setitem__(self, key = " ", value = 0):
        self.__dict__[key] = value

class Bill:
    def __init__(self, menu, order):
        pass


m = Menu()
m["idly"] = 20
m["vada"] = 20

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(e)

b = Bill(m, o)
print(b)
