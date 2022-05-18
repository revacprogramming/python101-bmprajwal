# Lists

filename = "romeo.txt"

fname = input("Enter file name: ")
fh = open(fname)

roll = list()
for line in fh :
    words = line.split()
    for word in words :
        if word not in roll:
            roll.append(word)

roll.sort()
print(roll)