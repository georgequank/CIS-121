###Today a new data type!
names = ["Kendrick", 2, 3, .45, 23]
#dictionaries
#a data type that we can store data by key
#to access data for names, example .45
print(names[2])

#to define an empty dictionary
info_empty = {}
#define a dictionary
info = {
    "Patient 0": ["Kendrick", "Morales", 23],
    "Patient 1": 23,
    "Patient 2": ["Bob", "Builder", 134]
}

#how to add values to dictionary
info["Patient 3"] = ["Roger", "NA", "NA"]

#print(info)

print(info["Patient 3"])

#-----------------------------------------------------------------------------------------------------------------------------------

#CREATE A SCRIPT THAT ASKS THE USER FOR THEIR NAME, LAST NAME, AND AGE. KEEP THIS INFO STORED IN A DICTIONARY, THEN PRINT VALUES

user_info = {
    "user1": [input("What is your first name?: "), input("What is your last name?: "), input("What is your age?: ")]
}

print("Your name is", user_info["user1"[0]], user_info["user1"[1]], "you are", user_info["user1"[2]], "years old")

#-----------------------------------------------------------------------------------------------------------------------------------
#Create a script that ask the iuser for 5 soccer players and how many goals they made this season.
#Calculate the average in a seperate function.


def avg_goals(players):
    sum = 0
    for player in players:
        sum += players[player]
    return sum/len(players)

players = {}

for i in range(5):
    name = input("Please enter players name: ")
    goals = int(input("Please enter how many goals they scored this seaseon: "))

players[name] = goals

print("The average goals was:", avg_goals(players))

#-----------------------------------------------------------------------------------------------------------------------------------
#CREATE A FUNCTION THAT VERIFIES IF A KEY ALREADY EXISTS IN YOUR DICTIONARY

dictionary1 = {
    "Info_1": ["Ray", "Deml", 21],
    "Info_2": ["Yar", "Lmed", 12]
}

def key_check(dictionary, key):
    for key_value in dictionary:
        if key_value == key:
            return True
    return False

print(key_check(dictionary1, input("What key are you checking: ")))

#-----------------------------------------------------------------------------------------------------------------------------------

info1= {
    "data": [1, 2, 3, 4, 5]
}
info2= {
    "data": [6, 7, 8, 9, 10]
}

def add_together(data, data2):
    total = []
    for i in range(len(data["data"])):
        total.append(data["data"][i] + data2["data"][i])
    print(total)

add_together(info1, info2)