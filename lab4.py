#inputs of upper and lower bounds
lowerBound = 1
upperBound = int(input("Enter an upper bound: "))
numberCheck = lowerBound
divisor = 0
proper = 0
deficient = 0
perfect = 0
abundant = 0
#outside loop adds 1 to the number that it is checking
#on the inside loop:
#the first part finds proper divisors for the number it is checking
#the second part takes those proper divisors and adds them together, if they are the same as the number being checked, it adds one to the perfect count
#the third part takes those proper divisors, adds them again, and if they are more than the number being checked, it adds one to the abundant count
#the last part takes propers again, adds them, and if they are less than the number being checked, it adds one to the deficient count
while lowerBound <= upperBound:
    while numberCheck < lowerBound:
        if lowerBound % numberCheck == 0:
            proper += numberCheck
            
        numberCheck += 1
        
    if proper == lowerBound:
        perfect += 1
    elif proper < lowerBound:
        deficient += 1
    elif proper > lowerBound:
        abundant += 1
    lowerBound += 1

    proper = 0
    numberCheck = 1
#printing results
print("Between", lowerBound, "and", upperBound, "there are")
print(deficient, "dificient numbers")
print(perfect, "perfect numbers")
print(abundant, "abundant numbers")