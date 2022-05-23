# Tuples

filename = "mbox-short.txt"
fhand = open(filename)

sike = dict()

for line in fhand :
    if line.startswith('From:'): continue
    if not line.startswith('From'): continue

    words = line.split()
    time = words[5]
    hour = time[:2]
    sike[hour] = sike.get(hour, 0) + 1

for key, value in sorted(sike.items()):
    print(key, end=' ')
    print(value)
