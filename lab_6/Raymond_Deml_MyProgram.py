###opening file
file = open("500DayFruitData1.txt", 'r')
import Raymond_Deml_Stats

#Getting all the lines and seperating them by /n
data = file.read().splitlines()
data.pop(0)
apple_tracker = []
banana_tracker = []
strawberry_tracker = []

for item in data:
    temporary = item.split()
    if temporary[1] == "apple":
        apple_tracker.append(int(temporary[2]))
    elif temporary[1] == "banana":
        banana_tracker.append(int(temporary[2]))
    elif temporary[1] == "strawberry":
        strawberry_tracker.append(int(temporary[2]))

apple_mean = str(Raymond_Deml_Stats.mean(apple_tracker))
apple_median = str(Raymond_Deml_Stats.median(apple_tracker))
banana_mean = str(Raymond_Deml_Stats.mean(banana_tracker))
banana_median = str(Raymond_Deml_Stats.median(banana_tracker))
strawberry_mean = str(Raymond_Deml_Stats.mean(strawberry_tracker))
strawberry_median = str(Raymond_Deml_Stats.median(strawberry_tracker))


#creating a new file
with open("Raymond_Deml_Output.txt", 'w') as f:
    f.write("The mean number of apples eaten is: " + apple_mean + "\n" "The median number of apples is: " + apple_median + "\n" + "The mean number of bananas eaten is: " + banana_mean + "\n" + "The median number of bananas eaten is: " + banana_median + "\n" + "The mean number of strawberries eaten is: " + strawberry_mean + "\n" + "The median number of strawberries eaten is: " + strawberry_median)

#make it work for bananas and strawberries!