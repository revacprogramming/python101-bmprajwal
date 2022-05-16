# Functions

def computepay(hours, rate):
    if hours<=40 :
        pay = hours*rate
    else :
        h = hours - 40
        pay = (40*rate) + (1.5*rate*h)
    
    return pay

hours = float(input('Enter the hours: '))
rate = float(input('Enter rate: '))

pay = computepay(hours, rate)
print(pay)