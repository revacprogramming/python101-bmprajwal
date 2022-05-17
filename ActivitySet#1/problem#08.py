fname = input('Enter the file name: ')

fl = open(fname)

count = 0
total = 0

for line in fl :
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        index = line.find('0.')
        total = total + float(line[index:index+7])
        avg = total/count 
        
print('Average spam confidence:',avg)