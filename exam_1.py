#Raymond Deml
#Exam 1
#I was in the back right table that got the bonus points for this exam

###1a
#This code does not run because the age input needs to be an integer
#or a float. I would fix this by adding an int to the front of the age input as follows:
#age = int(input ("Please enter your age:"))



###1b
#this code does not run because number is not defined as a variable. To fix this,
#I could, for example, define number as 5, but this would cause it to print forever.
#To not have it print forever, I could add 20 to the number on each run through the while loop.
#here's the full code that works:
#number = 5
#while number < 100:
#    number += 20
#    print(number)



###1c
#this code runs like it is supposed to.



###1d
#if the goal of this code is to print from 1 to 9, then it runs fine.



###1e
#if the goal of this program is to enter a number until the user enters 5, then a bit of a rework is
#needed. Here I used a while loop, and it still doesn't work :(
running = True
user_number = 0
while running == True:
    if user_number == 5:
        running = False
    else:
        user_number = int(input("Please enter a number: "))


###2
#getting inputs of how much of each grocery the customer wants
milk_count = int(input("How many gallons of milk do you want?: "))
egg_count = int(input("How many dozen eggs do you want?: "))
bacon_count = int(input("How many packages of bacon do you want?: "))
#calculating the price according to how many of each item the customer gets
milk_price = (milk_count * 2.00)
egg_price = (egg_count * 1.50)
bacon_price = (bacon_count * 3.00)
#this block of code prints out the results from calculating
#the last line also rounds the total to the nearest cent so its easier to understand
print("Your reciept:")
print(milk_count, "gallons of milk:", milk_price, "dollars")
print(egg_count, "dozen eggs:", egg_price, "dollars")
print(bacon_count, "packages of bacon:", bacon_price, "dollars")
print("Tax,", "11%")
print("Total price:", round(((milk_price + egg_price + bacon_price) * 1.11), 2), "dollars")



###3
#user input for phone number
phone_number = input("Please enter your 10-digit phone number without spaces or dashes: ")
#this if checks if the number is 10-digits like it is supposed to be
#otherwise the else tells the user to enter a correct number
if 999999999 < int(phone_number) <= 9999999999:
    print("(" + phone_number[0:3] + ")", phone_number[3:6] + "-" + phone_number[6:10])
else:
    print("You did not correctly enter your number")



###4
#this is to keep track of how many divisors
divisor_count = 0
#the outside for loop is for the range stated
for random_number in range(0, 60):
    #this checks if the number is even
    if random_number % 2 == 0:
        print(random_number)