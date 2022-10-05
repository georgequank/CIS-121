###
# names = ["Kendrick", "Gabriel"]
# random_stuff = [1, 1.2, False, [], "S"]

#indexing
#print(names[0])

# for name in random_stuff:
#     print(name)

#------------------------------------------------------------------------------------------------------------------

#create a script that creates the sentence from the following two lists:

# list1 = ["I", "your", "dude"]
# list2 = ["am", "boss", "."]
# blank_list = []

# for word_index in range(0, 3):
#     print(list1[word_index], list2[word_index], end=" ")
#the word index in the second line is that index value from the for loop, 0 through 3!
#the end changes the default \n with a space instead!
#so instead of:
#I
#am
#your
#it looks like thos:
#I am your

#------------------------------------------------------------------------------------------------------------------

#create a function that allows users to create 2 lists of len5. The user must type in only numbers (int)
#Once all 10 numbers have been added, create a third list with the sum of the same index values

# blank_list = []
# blank_list2 = []
# number_count = 0
# sum_list = [" ", " ", " ", " ", " "]

# while number_count <= 8:
#     for number_index in range(0,1):
#         blank_list.append(int(input("Enter a number: ")))
#         blank_list2.append(int(input("Enter a number: ")))
#         number_count = number_count + 2

# for number in range(0, 5):
#     sum_list[number] = (blank_list[number] + blank_list2[number])

# print(blank_list)
# print(blank_list2)
# print(sum_list)

#use .isdigit to check if the number entered is a digit! This is important to filter out strings

#------------------------------------------------------------------------------------------------------------------

#create a script that asks the user for 3 family members. then ask tbem what rank they give them from 1-3
#keep track of the rank in a seperate list

# name_list = []
# rank_list = []
# tracker_count = 0

# while tracker_count < 3:
#     name_list.append(input("Enter a family member: "))
#     rank_list.append(input("How do you rank them: "))
#     tracker_count += 1

# print("===RANKING===")
# for index in range(0, len(name_list)):
# #the len insures that I don't hard code the length of the list into the printing!
#     print(name_list[index], "-", rank_list[index])
# print("=============")

#------------------------------------------------------------------------------------------------------------------

