

def get_cs():
    cs = input()
    return cs


def cs_to_lot(cs):
    lst = []
    words = cs.split(';')
    for word in words:
        ind = word.split('=')
        lst.append(tuple(ind))
    
    return lst



def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
