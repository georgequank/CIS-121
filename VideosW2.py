#len and position
course = "CIS 121"
print(len(course))
print(course[2])
print(course[-1])
print(course[0:])

#this is an escape sequence
course2 = "CIS \n\"121\""
print(course2)

#formatting strings
first = "Ray"
last = "Deml"
full = f"{first} {last}"
full2 = first + " " + last
print(full)
print(full2)

full_upper = (full.upper())
print(full_upper)

#working with strings
#upper, capitalizes string
#lower, lowercase string
#title, capitalizes first letter in each word in a string
#strip, removes spaces from string
#lstrip/rstip, removes spaces from left or right of string
#find, finds index of string
#replace, replaces a letter with another:
print(full.replace("R", "M"))
print("Ray" in full)
print("Dine" not in full)