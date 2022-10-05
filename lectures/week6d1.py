###exam review
#1a
#needs to be an integer
#1b
#doesn't work because number is not defined
#1c
#correct
#1d
#needs to be indented
#1e
#needs to be integer
#2
#good
#3
#needs to be a function?
#4
#also needs to be a function, I did it completely wrong

#------------------------------------------------------------------------------------------------------------------

#ACTUAL NOTES
#need to do unit 3, 4, and 5 for exam 2

#new data types: liss

# names = ["Kendrick", "Gabriel", "Ray"]
# random_stuff = ["Ken", 1, 122.3, False, []]

# print(names[2])
# #going negative gives the last value!
# print(random_stuff[-1])

# for value in random_stuff:
#     print(value)


#------------------------------------------------------------------------------------------------------------------
#create a script that goes through this list [2, 45, 32, 43, 22] and display the square of every number


# def squarer():
#     list = [2, 45, 32, 43, 22]
#     for number in list:
#         print(number ** 2)
# squarer()

# #or we could do
# result =[]

#append always adds it to the BACK of the list
# for num in list:
#     result.append(num ** 2)
# print(result)

# #to get the length of the list
# print(len(list))

#------------------------------------------------------------------------------------------------------------------
#create a script that ask the user for theor anem, age and number
#add those values to a list and display them
# name = input("What is your name?: ")
# age = int(input("What is your age?: "))
# number = int(input("What is your number?: "))
# stat_list = [name, age, number]

# print(stat_list)

# print("Name: ", stat_list[0])
# print("Age: ", stat_list[1])
# print("Number: ", stat_list[2])

#------------------------------------------------------------------------------------------------------------------
#Create a script that creates a list without the number 20 in it [20, 34, 23, 2, 11, 24, 4, 20, 21, 12, 20, 20, 20]

number_list = [20, 34, 23, 2, 11, 24, 4, 20, 21, 12, 20, 20, 20]
empty_list = []

def twenty_deleter():
    for numb in number_list:
        if numb != 20:
            empty_list.append(numb)
    print(empty_list)

twenty_deleter()

