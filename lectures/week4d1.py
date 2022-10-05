#write a small script that asks a user for a number between 35 and 2000
#when the user enters the number, the program should print the numbers
#from that x numbers to 100.
#but if the number goes over 100, just print the 100 by itself

#x = int(input("What is a number between 35 and 1000?:"))

#if 35 <= x <= 1000:
#    while x < 99:
#        print(x)
#        x += 1
#        print(x)
#    print("100")
#else:
#    print("That number is not in the range")


#Kendrick's version of the problem
x = int(input("Enter a number between 35 and 1000: "))

if 35 <= x <= 1000:
    if x >=100:
        print(100)
    else:
        while x <= 100:
            if (x % 2) == 0:
                print(x)
            x += 1
else:
    print("Not a number in the range")

###BOOLEANS
#winner = True
#lose = False