###Lecture notes
###starting with problems

#problem 1
#write a function that creates two lists of random values. 
#The user should send as a parameter how many elements the list shoudl have
#createList(5)
#[2, 3, 4, 1, 3] [1, 2, 3, 4, 5]

import random
def double_random_list(number):
  list_1 = []
  list_2 = []
  for x in range(number):
    list_1.append(random.randint(1, 100))
    list_2.append(random.randint(1, 100))
  print(list_1)
  print(list_2)

double_random_list(5)

#=================================================================================

###write a function that finds how many times the letters "a" and "u"
###appear in a word. Return a dictionary with each amount

words = ["hello", "aheeuh", "good", "sussy baka"]

def a_u_finder(list):
  a_count = 0
  u_count = 0
  for key in list:
    for letter in key:
      if letter == "a":
        a_count += 1
      elif letter == "u":
        u_count += 1
  dictionary_count = {}
  dictionary_count["A"] = a_count
  dictionary_count["U"] = u_count
  print(dictionary_count)

a_u_finder(words)

#=================================================================================

##Write a function that asks the user for the 10 best 4 mile runs times
##calculate the average
store the 10 times, the avg, the 5 best times, and 5 worst times
import statistics
def runningCalc():
  times_list = []
  mean = 0
  empty_d = {}
  for time in range(0, 10):
    times_list.append(int(input("Enter your time for run: ")))
    mean = statistics.mean(times_list)
    
  empty_d["All times"] = times_list
  empty_d["Average"] = mean
  empty_d["Top 5"] = "placeholder"
  empty_d["Bottom 5"] = "placeholder"
  
  print(empty_d)
runningCalc()

def runTimes(list_of_times)

#=================================================================================

###write a function that takes 2 list and generate a dictionary
#then multiply all the values by 5 and create a new key for each multiplication
# [1, 2, 3,] ["Num", "Num 2", "Num 3"]

listA = [1, 2, 3]
listB = ["Num 1", "Num 2", "Num 3"]
new_d = {}

def multBy5(listA, listB):
  for i in range(len(listA)):
    new_d["Num " + str(i + 1)] = (listA[i] * 5)
  return new_d

print(multBy5(listA, listB))