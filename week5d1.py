###Exam 1 details
#5 questions whether code works or not
#3 normal questions, but shorter than the normal lab

#for loops
#number = 1
#for number in range(1,11):
#    if number % 2 == 0:
#        print(number)

#functions
#any variables and code inside the function, is in the SCOPE of the function
#because of this, you have to make a variable for that function
#def askUserForName():
#    name = input("Please Enter Your Name: ")
#    return name

#name = askUserForName()

#print("Your name is", name)

###create a function that asks the user for their age. Then use that value to print out the next 20 years
#(use a for loop)
#def askUserForName():
#    age = int(input("What is your age?: "))
#    return age
#age = askUserForName()
#for age in range(age, (age+21)):
#    print(age)

###string manipulation
#name = "Raymond"
#print(name[0:3])
#for letter in name:
#    print(letter)

#problem 1
#for num in range(6):
#    user = int(input("Enter a number"))
#    summ += user
#for i in range(summ, 2001):
#    if i % 2 == 1:
#        print(i)
#    if 96 % i == 0:
#        print("Found one!")

#problem 2
#user = int(input("How many dvds do you want?: "))
#summ = user * 3
#if summ >= 50:
#    print("You pay", summ - summ * .2)
#elif summ >= 30:
#    print("You pay", summ - summ * .1)
#else:
#    print("You pay", summ)

#problem 3

for i in range(1, 6):
    for j in range(1, i):
        print(j)
    print(" ")