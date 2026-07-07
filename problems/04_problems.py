# Q1. take name and age from user and print

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}")
print(f"you are {age} years old")

# Q2. user decimal number and integer number input kare

num1 = int(input("Enter integer number: "))
num2 = float(input("Enter floating number: "))
print(f"your integer number is: {num1}")
print(f"your floating number is: {num2}")

# Q3. take two number and use operators

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)

# Q4. print even or odd

num =  int(input("Enter your  number: "))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")

# Q5. positive , negative and zero

num = int(input("Enter the number: "))
if num < 0:
    print("negative number")
elif num == 0:
    print("zero")
else:
    print("positive number")

# Q6. Grade Calculator

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A: you are a brilliant student")
elif marks >= 80:
    print("B tou are very a good student")
elif marks >= 70:
    print("C: you are a good student")
elif marks >= 60:
    print("D: you just need guidence")
else:
    print("Fail: you just need extra classes to improve")

# Q7. print first 20 even number using for loop

for x in range(2, 42, 2):
    print(x)
    

# Q8. take number form user print table of that number

num = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")

# Q9. print the sum of 1 to 100

total = 0
for i in range(1,101):
    total +=i
    print(total)

