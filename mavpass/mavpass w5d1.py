#3 things

#what asked for?
#what givem?
#what are we using to do it?

#ask her what she is buying, the total amount of items
#given is 9% tax, 30% sale

# sale = .7
# tax = 1.09
# full_price = float(input("How much are the items you are buying: "))
# actual_total = 0

# actual_total = ((full_price * sale) * tax)
# print(actual_total)

#---------------------------------------------------------------------------------------------------

#ask for variables:
# length = float(input("What is the length of the hot tub in inches: "))
# width = float(input("What is the width of the hot tub in inches: "))
# height = float(input("What is the height of the hot tub in inches: "))

# #calculations
# total_volume = (length * width * height)
# convert_to_gallons = (total_volume / 231)

# #print results
# print(convert_to_gallons)

#---------------------------------------------------------------------------------------------------
#syntax, how to create
#why
#example

# def function():
#     #code
# function()


#make this a function

def function1():
    count = 0
    total = int(input("What are we counting towards?: "))
    while count < total:
        print(count)
        count += 1

def function2():
    function1()
    print("DONE!")
function2()