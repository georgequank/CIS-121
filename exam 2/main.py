###QUESTION 1

lyst = [1, 2, 3, 4, 2, 5, 2, 8, 21414]

###function takes a list as argument
def oddEvenLister(list):
  #make empty lists and dict for use in the loop
  odds = []
  evens = []
  dict_e = {}
  #this loop simply check if the key in argument list is even or odd, then appends it to
  #its list
  for key in list:
    if key % 2 == 0:
      evens.append(key)
    else:
      odds.append(key)
  #setting dictionary values
  dict_e["Odd"] = odds
  dict_e["Even"] = evens
  return dict_e

#call and print the results
print(oddEvenLister(lyst))

#==================================================================================

###QUESTION 2
#importing random and counter, which counts the elements in a list
import random
from collections import Counter

#list gen counter generates 2 lists, then counts how many values
#there is in each list
def listGenCounter():
  list_1 = []
  list_2 = []
  list_3 = []
  dictionary_e = {}
  for x in range(0, 200):
    list_1_numb = random.randint(1, 100)
    list_2_numb = random.randint(1, 100)
    #appending to each individual list, and then the third list
    #is both
    list_1.append(list_1_numb)
    list_2.append(list_2_numb)
    list_3.append(list_1_numb)
    list_3.append(list_2_numb)
  #counts the amount of values in each list
  list_1_count = Counter(list_1)
  list_2_count = Counter(list_2)
  list_3_count = Counter(list_3)
  #adds the dictionaries generated from counter into one big dictionary
  dictionary_e["LIST 1 COUNTS"] = list_1_count
  dictionary_e["LIST 2 COUNTS"] = list_2_count
  dictionary_e["COMBINED LIST COUNTS"] = list_3_count
  #writes to a file, RESULTS4.txt
  with open("RESULTS4.txt", "w") as file:
    file.write("LIST 1 COUNTS" + "\n" + str(dictionary_e["LIST 1 COUNTS"]) + "\n" + "LIST 2 COUNTS" + "\n" + str(dictionary_e["LIST 2 COUNTS"]) + "\n" + "COMBINED LIST COUNTS" + "\n" + str(dictionary_e["COMBINED LIST COUNTS"]))
  #if needed
  return dictionary_e
listGenCounter()

#==================================================================================
#QUESTION 3
import statistics

def stepAvg(file):
  #month lists
  month_list = []
  jan = []
  feb = []
  mar = []
  apr = []
  may = []
  jun = []
  jul = []
  aug = []
  sep = []
  oct = []
  nov = []
  dec = []
#open and read file
  file_open = open(file, 'r')
  file_read = file_open.read()
  file_split = file_read.splitlines()
  print(file_split)
  #grab the keys in the ranges of the split file, then adds it to each lists
  for key in range(334, 365):
    dec.append(key)
  for key in range(304, 334):
    nov.append(key)
  for key in range(273, 304):
    oct.append(key)
  for key in range(243, 273):
    sep.append(key)
  for key in range(212, 243):
    aug.append(key)
  for key in range(182 ,212):
    jul.append(key)
  for key in range(151 ,182):
    jun.append(key)
  for key in range(121, 151):
    may.append(key)
  for key in range(90, 121):
    apr.append(key)
  for key in range(60 ,90):
    mar.append(key)
  for key in range(32, 60):
    feb.append(key)
  for key in range(0, 32):
    jan.append(key)

  #calculates means
  jan_mean = statistics.mean(jan)
  feb_mean = statistics.mean(feb)
  mar_mean = statistics.mean(mar)
  apr_mean = statistics.mean(apr)
  may_mean = statistics.mean(may)
  jun_mean = statistics.mean(jun)
  jul_mean = statistics.mean(jul)
  aug_mean = statistics.mean(aug)
  sep_mean = statistics.mean(sep)
  oct_mean = statistics.mean(oct)
  nov_mean = statistics.mean(nov)
  dec_mean = statistics.mean(dec)

  #makes a table
  table = ("MONTH".ljust(12) + "|" + "AVERAGE".rjust(12) + "\n" + "January".ljust(12) + "|" + str(jan_mean).rjust(12) + "\n" + "Febuary".ljust(12) + "|" + str(feb_mean).rjust(12) + "\n" + "March".ljust(12) + "|" + str(mar_mean).rjust(12) + "\n" + "March".ljust(12) + "|" + str(mar_mean).rjust(12) + "\n" + "April".ljust(12) + "|" + str(apr_mean).rjust(12) + "\n" + "May".ljust(12) + "|" + str(may_mean).rjust(12) + "\n" + "June".ljust(12) + "|" + str(jun_mean).rjust(12) + "\n" + "July".ljust(12) + "|" + str(jul_mean).rjust(12) + "\n" + "August".ljust(12) + "|" + str(aug_mean).rjust(12) + "\n" + "September".ljust(12) + "|" + str(sep_mean).rjust(12) + "\n" + "October".ljust(12) + "|" + str(oct_mean).rjust(12) + "\n" + "November".ljust(12) + "|" + str(nov_mean).rjust(12) + "\n" + "December".ljust(12) + "|" + str(dec_mean).rjust(12))
  #puts it in a new file called month.txt
  with open("month.txt", "w") as file:
    file.write(table)

stepAvg("steps.txt")