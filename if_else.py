# Do some code only if some condition is true else do something false....

age = int(input("Enter you age: "))
if age >= 70:
    print("you can retire")
elif age >= 18:
    print("you can vote")
elif age < 0:
    print("you haven't been born yet")
else:
    print("you cannot vote")