# Set ek collection hai jo sirf unique values store karta hai.
# Set unorderd hota hai 

# pyhton remove duplicate value automatically
number = {10,20,30,40,50,10,10,20,30}
print(number) 


# num = [1,2,3,4,5]
# print(num[2]) ==> result 3

# num = {1,2,3,4,5}
# print(num[2])  ==> type error

numbers = {12,34,21}
numbers.add(43)
numbers.update([10,20])
numbers.remove(12)
numbers.pop()
print(numbers)
# add()     → ek value
# update()  → multiple values

student = {
    "shadik",
    "rahul",
    "aman",
    "ganesh"
    
}
print("shadik" in student)  # ==> True
print("jagdish" in student) # ==> False


python_club = {"Rahul","Shadik","Aman"}
ai_club = {"Aman","Rohit","Shadik"}
print(python_club | ai_club)
print(python_club & ai_club)
print(python_club - ai_club)


logged_in = {
    "shadik",
    "rahul",
    "jagdish"
}
user = "shadik"
if user in logged_in:
    print("Already Logged In")
else:
    print("Login First")
    
    
# Set unique values store karta hai.
# Duplicate automatically remove ho jate hain.
# Set unordered hota hai.
# Indexing nahi hoti.
# add() ek value add karta hai.
# update() multiple values add karta hai.
# in operator aur Union/Intersection jaise operations ke liye Set bahut useful hai.