# Problem 5 - Can you remove duplicates from an array?

array =[2,5,7,8,3,2,8,9,3]
newArray=[]

for i in range(0,len(array)):
    count=0
    for j in range(i+1,len(array)):
        if(array[i]==array[j]):
            count+=1
    if(count==0):
        newArray.append(array[i])

print(newArray)