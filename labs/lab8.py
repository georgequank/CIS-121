###Lab 8

#this function takes the file name, grabs its contents, splits it by lines,
#then appends to an empty list if that "line" is a digit
def digitLister():
  list_1 = []
  file = open("randomValues.txt", "r")
  file_contents = file.read()
  split_contents = file_contents.splitlines()
  for key in split_contents:
    if key.isdigit():
      list_1.append(int(key))
  return list_1
  
data = digitLister()
print(data)

#finds the minimum value
def findMin(index, currentMin, data):
  if len(data) == 0:
    print("Empty lists cannot be worked with")
  if len(data) == 1:
    return data[0]
  min = data[index]
  if min <= currentMin:
    currentMin = min
  if index >= len(data) - 1:
    return currentMin
  else:
    return findMin(index + 1, currentMin, data)

print(findMin(0, data[0], data))

#finds the maximum value
def findMax(index, currentMax, data):
  if len(data) == 0:
    print("Empty lists cannot be worked with")
  if len(data) == 1:
    return data[0]
  max = data[index]
  if max >= currentMax:
    currentMax = max
  if index >= len(data) - 1:
    return currentMax
  else:
    return findMax(index + 1, currentMax, data)

print(findMax(0, data[0], data))

#find extrema

def findExtrema(data, calculate_min=True, calculate_max=True):
  if calculate_min == True and calculate_max == True:
    return [findMin(0, data[0], data), findMax(0, data[0], data)]
  elif calculate_min == False and calculate_max == False:
    return ["Nothing was done"]
  elif calculate_min == False:
    return [findMax(0, data[0], data)]
  elif calculate_max == False:
    return [findMin(0, data[0], data)]

print(findMin(0, data[0], data))
print(findMax(0, data[0], data))
print(findExtrema(data))
print(findExtrema(data, False))
print(findExtrema(data, False, False))