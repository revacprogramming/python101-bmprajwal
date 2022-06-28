def input_set():
    return input('Enter the elements of set: ').split(' ')

def get_operation():
    return input('Enter the operation (n/u)? ')

def get_operands():
    operands = input('Enter the operands (set1, set2, set3): ').split(' ')
    l1 = list()
    l1.append(set1)
    l1.append(set2)
    l1.append(set3)

    if 'set1' not in operands:
        l1.pop(0)
    elif 'set2' not in operands:
        l1.pop(1)
    elif 'set3' not in operands:
        l1.pop(2)

    return l1

def perform_operations(operation, *operands):
    if operation == 'u':
        union_set = set()
        for operand in operands:
            union_set.update(operand)
        return union_set

    elif operation == 'n':
        inter_set = filter(lambda x:x in operands[0],operands[1])
        if len(operands) == 3:
            return set(filter(lambda x:x in inter_set, operands[2]))
        return set(inter_set)
      
## Main program starts here ##
def main():
    global set1, set2, set3
    set1 = input_set()
    set2 = input_set()
    set3 = input_set()
    operation = get_operation()
    operands = get_operands()
    result = perform_operations(operation, *operands)
    print(result)

if __name__ == '__main__':
    main()

