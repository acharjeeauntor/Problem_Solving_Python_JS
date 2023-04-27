# Problem 2: How do you find a missing number in an array of 1-100?

array = [4,5,6,10,90,50]
count=0
missingNumberArray=[]

for num in range(1,100+1):
    for i in range(0,len(array)):
        if(num==array[i]):
            count+=1
    if(count==0):
        missingNumberArray.append(num)
    else:
        count=0
    
print(f"The missing Numbers are: {missingNumberArray}")