# Typecasting = the process of converting a variable from one datatype to another 
#                           str(), int(), float(), bool(),

name = "bro code"
age = 21
gpa = 7.4
isStudent = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(isStudent))

gpa = int(gpa)
print(gpa)

gpa = float(gpa)
print(gpa)

age = float(age)
print(age)

#  name = float(name) #Error => could not convert String into float datatype
# print(name)

# name = int(name) #Error => could not convert String into int datatype
# print(name)

age = int(age)
age += 1
print(age)

name = bool(name) #=> True
print(name)


gpa = str(gpa)
print(gpa)
