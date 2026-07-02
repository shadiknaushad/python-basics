import math

# 1. print circumference of circle

radius = float(input("Enter the radius of circle: "))
circumference = 2 * math.pi * radius
print(f"the circumference is: {circumference}")

# 2. print the area of triangle

height = float(input("Enter the height of triangle: "))
base = float(input("Enter the base of triangle: "))
area = 0.5 * base * height
print(f"the are of triangle is: {area}")

# 3. Area of circle

radius = int(input("enter the radius of circle: "))
area = math.pi * math.pow(radius,2)
print(f"area of circle is: {area} ")

# pythogourus theorem

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"side c is: {c}")