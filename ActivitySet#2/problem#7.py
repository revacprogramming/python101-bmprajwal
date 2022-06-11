

class Menu:
    def __init__(self, food = '', price = 0):
        self.menu = list()
        self.menu.append((food,price))
    
    def __add__(self, i):
        self.menu.append((i[0], i[1]))
        return self
    

    def __str__(self):
        fmenu = self.menu[1:]
        return ('\n'.join([str(i + ' ' + str(j)) for i,j in fmenu]))
        



m = Menu()
m = m + ("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

print(m)  # should print the menu properly
