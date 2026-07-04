# Conditional Statement = A one-line shortcut for the if_else statement (ternary operator)
#                         print or assign one of two values based on a condition
#                          X if condition else Y

num = 10
print("positive" if num > 0 else " negative")

num = 52
print("even" if num % 2 == 0 else "odd")

age = int(input("Enter your age: "))
print("you can vote" if age >=18 else "you cannot vote")