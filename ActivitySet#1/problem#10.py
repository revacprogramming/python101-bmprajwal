# Dictionaries

filename = 'mbox-short.txt'
fhand = open(filename)

dick = dict()

for line in fhand :
    if line.startswith('From:') : continue
    if not line.startswith('From') : continue

    word = line.split()
    dick[word[1]] = dick.get(word[1], 0) + 1

maxkey = None
maxval = None

for key, value in dick.items() : 
    if maxval is None or maxval < value:
        maxval = value
        maxkey = key

print(maxkey, maxval)
