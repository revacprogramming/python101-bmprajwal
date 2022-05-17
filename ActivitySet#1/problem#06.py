# Loops & Iterators

largest = None
smallest = None

while True:
    num = input("Enter a number? ")
    if num == "done":
        break
    try:
        n = int(num)
        if largest  or n > largest:
            largest = n
        if smallest  or n < smallest:
            smallest = n
    except:
            print('Invalid input')

print('Maximum is '+str(largest))
print('Minimum is '+str(smallest))
        
    

