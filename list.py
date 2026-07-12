# collection = single "variables" used to store miultiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} inordered and immutable, but add/remove OK , not duplicate
# Tuple = () ordered and unchengeable , duplicates Ok, FASTER

fruits = ["apple", "banana", "mango", "coconut", "cherry"]
print(fruits[1:3])
print(fruits[:3])
print(fruits[1:])
print(fruits[-1:-3])
fruits[1] = "bluebarry" # change banana to bluebarry
print(fruits)
print(fruits[::-1])
for fruit in  fruits:
    print(fruit)

num = [10,20,20,40]
print(num[0]) # Accessing the first element
print(num[1]) # Accessing the second element
print(num[2]) # Accessing the thrid element
print(num[3]) # Accessing the fourth element
print(len(num))

num = [10,20,30,40]
num.append(50)
print(num)

num.insert(2, 100)
print(num)

num.remove(10)
print(num)

num.clear()
print(num)

num.pop(2)
print(num)

num.sort()
print(num)