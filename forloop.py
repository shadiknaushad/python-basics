# For loop = execute a block of code a fixed number of time.
#            you can iterate over a range, String, sequence, etc...

for x in range(1 , 11):
   print(x)
   

for x in range(1 , 21):
    if x == 15:
        continue
    else:
     print(x)



for x in range(1 , 21):
    if x == 15:
        break
    else:
     print(x)