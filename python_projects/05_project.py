# pyhton compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <=0:
     print("principle can't be negative or equal to zero")
     

while rate <= 0:
    rate = float(input("Enter the innterest rate: "))
    if rate <=0:
     print("rate can't be negative or equal to zero")
     

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <=0:
     print("time can't be negative or equal to zero")
     
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years: {total:.2f}")
