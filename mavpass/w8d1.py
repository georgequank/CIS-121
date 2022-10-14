###open a file, read it, write 
#a to append to that file
###mavpass test 2 review
###activity 1 - brain dump! (our group did add to)

import random

###word problem 1
# def funct():
#   dict_e = {}
#   for i in range(1, 201):
#     dict_e[i] = random.randint(0, 101)

#   id = int(input("What is the customer's id that used a discount?: "))
#   print(dict_e[id])
#   dict_e[id] = 0
  
#   dict_e = str(dict_e)
#   print(dict_e)
  
#   with open("Customer discounts", "w") as file:
#     file.write(dict_e)
#   return dict_e

# funct()

###word problem 2
#added the remove customer problem

###problem 3
list = []
dict1 = {}
for i in range(1, 201):
  list.append(random.randint(1, 101))
print(list)

print(list[0])

for key in range(0, 199):
  if (key + 1) % 2 != 0:
    dict1[list[key]] = (key)

print(dict1)