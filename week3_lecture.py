#create a script that asks the user for their income.
#If the income is greater than 450000, print damn you rich
#If the income is less than that, print you got it

#input
#income = float(input("What is your income?: "))

#conditional
#if income > 450000:
#    print("Damn you rich!")
#elif income < 450000:
#    print("You got it!")

#-----------------------------------------------------------------------------------
#Create a guessing game. Give the user 3 chances. If they get it right print "yay"
#If not make a custom message
#input of a integer

tries = 1

#conditional
while tries < 4:
    guess = int(input("Guess a number: "))
    if guess == 5:
        print("You guessed it correct")
        tries = tries + 5
    else:
        print("Guess again")
        tries += 1

