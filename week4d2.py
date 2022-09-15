#number = 1
#finished = True #Boolean, remember to be capitalized

#if finished == True:
#    print("this is true")
#elif finished == False:
#    print("this is false")
#above is an example of a nested if statement
#if finished == True:
#    print("this is true")
#if finished == False:
#    print("this is false")
#this is not a nested conditional

#while number == 1:
#    number += 1
#while loop


#write a script that keeps asking the user for a number and check if the number is even or odd.
#Let the user know what it is. If they enter the number 0, stop asking
#running = True

#while running == True:
#    number = int(input("Enter a number: "))
#    if number == 0:
#        running = False
#        print("That is a 0, BYE!")
#    elif (number % 2) != 0:
#        print("Your number is odd")
#    elif (number % 2) == 0:
#        print("Your numer is even")

#create a script that asks the user for their name and income, let the user know how much money they would have
#if they dont spend any money in 20 years.
#Hey name, you make income a year! this is how much money you would have in 20 years
#40,000 year 1
#80,000 year 2
#40,000 * 20 year 20
#modify so that it lets the person know how many years to reach 10,000

name = input("What is your name?: ")
income = int(input("What is your income: "))
running = True
year = 1

print("Hello", name,"you make", income, "per year,", "This is how long it will take to reach $10,000!")

while (running == True):
    year += 1
    print("You have made", income * year, "dollars so far by year", year)
    if income * year >= 10000:
        running = False
        print("It took", year, "years to reach $10,000")