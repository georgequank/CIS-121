###remember random for test
import random

#lists
# names = ["Kendrick"]

# #dictionaries
# info = {
#   "Ken": 23
# }

#=================================================================================

##create a function that takes 2 lists, and makes them a dictionary
# [1, 2, 3]
# ["Number 1", "Number 2", "Number 3"]

list_1 = [1, 2, 3]
list_2 = ["Number 1", "Number 2", "Number 3"]
dictionary_1 = {}

def dictionary_maker():
  for key in range(0, len(list_1)):
    dictionary_1[list_1[key]] = list_2[key] 
  print(dictionary_1)
dictionary_maker()

#Kendrick's version
def createDictionary(keys, data):
  temp = {}
  if len(data) == len(keys):
    for i in range(len(keys)):
      temp[keys[i]] = data[i]
  return temp

print(createDictionary(list_1, list_2))

#=================================================================================

###create a function that can multiply all the numbers in a dictionary by
###a given number, make sure that these values are numeric

numbers = {
  "Numb 1": "12",
  "Num 2": "abcs",
  "Num 3": "56"
}

def numberMult(number_dict, number):
  temp_dict = {}
  for key in number_dict:
    if number_dict[key].isdigit():
      temp_dict[key] = (int(number_dict[key]) * number)
  return temp_dict

print(numberMult(numbers, 8))

#=================================================================================

###create a function that generates a dictionary with 5 numbers then  Then make
###another function that generates random numbers until it generates one
###inside of the dictionary

def createDict():
  temp = {}
  for i in range(5):
    temp["Number" + str(i + 1)] = i * 2
  return temp
print(createDict())

def getData(data):
  temp = []
  for i in data:
    temp.append(data[i])
    return temp

def guessNumber(data):
  guess = False
  temp = []
  values = getData(data)
  while guess != True:
    random_number = random.randint(1, 1000)
    if random_number in values:
      print("Found one! ", random_number)
      guess = True
      
x = createDict()
print(x)
guessNumber(x)