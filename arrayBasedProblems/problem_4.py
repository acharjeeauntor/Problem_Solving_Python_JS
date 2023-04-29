# Problem 4 : Can you find duplicate numbers in an array?

array = [3,6,8,8,3,10,10,0,4,2,7,8]
duplicateArray=[]

for i in range(0,len(array)):
    count=0
    for j in range(i+1,len(array)):
        if(array[i]==array[j]):
            count+=1
    if(count!=0):
        duplicateArray.append(array[i])

print(duplicateArray)