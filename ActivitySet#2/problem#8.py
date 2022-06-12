

class Menu(dict):
    def __setitem__(self, key='',value=0):
        self.__dict__[key] = value

    def __str__(self):
        return ('\n'.join([str(i + ' ' + str(j)) for i, j in self.__dict__.items()]))


m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)
