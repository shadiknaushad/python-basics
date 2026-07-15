def greet():
    print("Hello")
greet()
greet()
greet()
greet()

def welcome():
    print("welcome to pyhton")
welcome()
  
def add():
    print(10 + 20)
add()

def add(a,b):
    return a+b
result = add(10,20)
print(result)

def sum(a,b):
    add = a+b
    print("The sum is:", add)
sum(10,20)
sum(30,50)
sum(50,50)
print("End of he function call")

def sum(a,b):
    return a+b
x = sum(2,3)
print(x)
    
def salary(hours,rate):
    return hours * rate
pay = salary(8 , 500)
print(pay)

def even_odd(num):
    if num %2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_odd(10))
print(even_odd(23))

def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "wrong username and password"
print(login("admin" , "1234"))
print(login("rahul" , "4321"))

# mini calculator using function
def calculator(a , b , operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b
    else:
        return "You enter the wrong operator"
print(calculator(10,5,"+"))
print(calculator(10,5,"-"))
print(calculator(10,5,"*"))
print(calculator(10,5,"/"))
print(calculator(10,5,"#"))



        
    


    
    