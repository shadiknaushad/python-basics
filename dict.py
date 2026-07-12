# Dictionaries in Python
# A dictionary (dict) is a built-in Python data structure that stores data
# in key-value pairs.

# word => meaning
# key  => value

# Creating a Dictionary
student = {
    "name": "Shadik",
    "age": 22,
    "branch": "CSE AIML",
    "course": "python programming"
}
student["college"] = "intergal university"
print(student)
print(type(student))

# Method 2
student = dict(name = "shadik" , age = 21 , city = "lucknow")
print(student)

# Accessing value
student = {
    "name": "shadik",
    "age": 21,
    "college": "Integral University"
}
print(student["name"])
print(student["age"])
print(student["college"])

# if key doesn't exist
student = dict(name = "shadik" , age = 21 , city = "lucknow")
print(student.get("phone")) # ===> return none

 # Adding , updating , delating 
student = {
    "name": "shadik",
    "age": 21,
    "college": "Integral University"
}
student["branch"] = "cse in aiml"
student["age"] = 22
del student["college"]
print(student)

# Dictionary Methods
student = {
    "name": "shadik",
    "age": 21,
    "college": "Integral University"
}
print(student.keys())
print(student.values())
print(student.items())
print(student.pop("name"))
print(student.clear())

# Looping Through a Dictionary
student = dict(name = "shadik" , age = 21 , city = "lucknow")
for key in student:
    print(key)
for value in student.values():
    print(value)
for key,value in student.items():
    print(key, ":", value)

# Nested Dictionary
students = {
    "student1":{
        "name": "Shadik",
        "age": 21,        
    },
    "student2":{
        "name": "rahul",
        "age": 22,
    }
}
print(students["student1"],students["student2"])








