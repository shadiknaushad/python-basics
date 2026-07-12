# tuple is immutable cannot be changed

num = (10,20,30,7.5,"mohit",True,False)
print(num)
print(type(num))
num[2] = 100 # error => tuple cannot be changed
print(num)
print(num[1:3])

num = (10,34,56,32,10,34,10)
num.index(10)
print(num.count(10))


