"""
Raymond Deml
9/8/2022

Description of what this program does
"""
import sys


taxOwed = 0.0

earnedIncome = float(input("Enter the amount of income you earned in 2021: "))
if earnedIncome < 0:
	print("You made less than $0. Contact an accountant")
	sys.exit()

print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")


#Ensures you have a valid marital status
while maritalStatus != "m" and maritalStatus != "s":
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")




# Your code goes here

#used for turning off the end message when income tax cannot be computed
end_message = 1

# Conditional bracket for basaed on marital status and income earned. 
# Tax owed is then set based on the criteria given by the lab sheet
# the outer bracket checks the marital status then send it to another bracket inside.
# These inner brackets check the income, then set the taxowed based on the lab sheet.
# If the income is outside the lab sheet, it will print an error message, then turn off the end message
# Once it does its filtering, and if the end message is active, it will display what your income tax is rounded
# added a new way that takes the previous amount, and minuses off of the income before taking
# its own bracket rate, then adds the amount minused by the previous bracket's rate

if maritalStatus == "s":
	if 0 <= earnedIncome <= 9950:
		taxOwed = earnedIncome * 0.10
	elif 9551 <= earnedIncome <= 40525:
		taxOwed = ((earnedIncome - 9950) * 0.12) + (9950 * 0.10)
	elif 40526 <= earnedIncome <= 86375:
		taxOwed = ((earnedIncome - 40525) * .22) + ((40525 - 9950) * 0.12) + (9950 * .10)
	else:
		print("We cannot compute this income tax")
		end_message = 0
elif maritalStatus == "m":
	if 0 <= earnedIncome <= 19900:
		taxOwed = earnedIncome * 0.10
	elif 19901 <= earnedIncome <= 81050:
		taxOwed = ((earnedIncome - 19900) * 0.12) + (19900 * 0.10)
	elif 81051 <= earnedIncome <= 172750:
		taxOwed = ((earnedIncome - 81050) * 0.22) + ((81050 - 19900) * 0.12) + (19900 * .10)
	else:
		print("We cannot compute this income tax")
		end_message = 0
if end_message == 1:
	print("This year you owe", taxOwed, "in taxes")