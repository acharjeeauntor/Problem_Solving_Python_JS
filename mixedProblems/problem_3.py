# Problem 3: How do you get the matching elements in an integer array?

myIntArray = [1,3,4,6,7,1,7,3,4,9,0]
machingElement = []

for m in range(0,len(myIntArray)):
    for n in range(m+1,len(myIntArray)):
        if (myIntArray[m] == myIntArray[n]):
            machingElement.append(myIntArray[m])

print(machingElement)