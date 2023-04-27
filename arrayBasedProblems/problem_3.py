# Problem 3: How do you reverse an array in place in python?

array=[5,8,9,4,10,5,3,7]
reversedArray = []

for i in range(0,len(array)):
    reversedArray.append(array[len(array)-1-i])

print(reversedArray)
