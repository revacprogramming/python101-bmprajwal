# Conditional Execution

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate per hour: "))
if hrs<=40:
    print(hrs*rate)
else:
    h=hrs-40
    print((40*rate)+(h*1.5*rate))
