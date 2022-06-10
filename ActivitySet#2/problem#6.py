

class Menu:
    

    def __init__(self):
        self.menu = list()

    def add(self,food, price):
        self.menu.append((food,price))

    def show(self):
        for i,j in self.menu:
            print(i,j)
        


m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada", 20)

m.show()
