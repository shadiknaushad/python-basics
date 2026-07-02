# Shopping cart program

item = input("What item would you like yo buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity
print(f"you have bought {quantity} * {item}/s")
print(f"your total is: ${total}")