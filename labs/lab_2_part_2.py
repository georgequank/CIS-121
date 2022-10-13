###do part 1B, 2B, and 3B of the lab from Thursday

#PART 1B
#conversion to dog years based on 1 human year
dog_convert = 7
#input request takes the human age as a float
human_age = float(input("Enter your age: "))
#calculation of dog age as a float, takes human_age and converts it to dog age (in days, or 1/360 of a year)
dog_age = round(human_age * dog_convert * 360)
#calculation of converting this float into years, months, then days. It uses quotient to get rid of the pesky remainder
dog_years = (dog_age // 360)
dog_months = ((dog_age - (dog_years * 360)) // 30)
dog_days = (dog_age - (dog_months * 30) - (dog_years * 360))
#what message to put into the next step
dog_message = "Your age in dog years is:"
#this converts dog_age to a string and adds it to "age in dog years", then prints it all
print(dog_message, dog_years, "years,", dog_months, "months and", dog_days, "day(s)!")
#----------------------------------------------------------------------------------------------------------------------------------------------
#PART 2B
#this is pretty much the same thing but instead of 1 human year being equal to 7 dog years, 1 human year is 1/9 of a cat year
#cat conversion
cat_convert = (1 / 9)
#for simplicity, I use the same human age input fomr the last program
#multiply cat age into the nearest day
cat_age = round(human_age * cat_convert * 360)
#like the last problem, this section make use of the quotient to calculate years, months, and days
cat_years = (cat_age // 360)
cat_months = ((cat_age - (cat_years * 360)) // 30)
cat_days = (cat_age - (cat_months * 30) - (cat_years * 360))
#cat message like the last problem for next step
cat_message = "Your age in cat yaers is:"
#print results
print(cat_message, cat_years, "years,", cat_months, "months and", cat_days, "day(s)!")
#----------------------------------------------------------------------------------------------------------------------------------------------
#PART 3B
#since these problems are similar except for the animal conversion, I'll keep these comments simple
#conversion
horse_convert = (3 * ((((human_age ** 2) - 47) / 7) + 12))
#horse age rounded to the nearest day
horse_age = round(horse_convert * 360)
#calculate horse years, months, days
horse_years = (horse_age // 360)
horse_months = ((horse_age - (horse_years * 360)) // 30)
horse_days = (horse_age - (horse_months * 30) - (horse_years * 360))
#message
horse_message = "Your age in horse years is:"
#print results
print(horse_message, horse_years, "years,", horse_months, "months and", horse_days, "day(s)!")
print(horse_convert)