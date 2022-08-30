temperature = 1
if temperature > 30:
    print("its warm")
elif temperature > 20:
    print("its nice")
else:
    print("its cold")
print("Done")

age = 11
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

#logical operators
high_income = True
good_credit = True
student = False
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
print("Done")

#age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("Eligible")
else:
    print("Not Eligible")
print("Done")