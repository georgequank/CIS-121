###
# names = ["Kendrick", "Morales"]
# info = {
#     "Kendrick": 23,
#     "Bob": 3456
# }

# #opening writing creating files
# #opening a file, storing it as variable file
file = open("data.txt", 'r')
# #to get the data from a file
# #use splitlines to not include the \n for every new line!
data = file.read().splitlines()
# print(data)

#create a function that takes a list of values in str and returns a new list with only int.

def conv_to_int():
    temp = []
    for number in data:
        if number.isdigit():
            temp.append(int(number))
    return temp

print(conv_to_int())

###create a function that takes the numbers and adds 5 to them.
def add_five():
    new_list = []
    for number in temp:
        new_list.append(number + 5)