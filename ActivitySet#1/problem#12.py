# Regular Expressions
# https://www.py4e.com/lessons/regex

import re

# filename = 'regex_sum_1548401.txt'
# fhand = open(filename, "r")

# lst = list()

# for line in fhand :
#   line = line.rstrip()
#   ls = re.findall('([0-9]+)', line)
#   # lst.append(ls)
#   lst += ls

# # la = [int(i) for i in lst]

# sum = 0
# for i in lst :
#   sum += int(i)

# # for i in la:
# #   sum += i
#print(sum)

print(sum([int(i) for i in (re.findall('[0-9]+', (open('regex_sum_1548401.txt','r').read())))]))