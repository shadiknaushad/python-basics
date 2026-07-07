# nested loop = a loop within another loop(outer , inner)

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbols = input("Enter the symbols to use: ")
for x in range(rows):
    for y in range(columns):
        print(symbols, end="")
    print()