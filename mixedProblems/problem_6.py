# Problm 6: How would you find the second largest number in an array?

array = [2,54,7,98,3,8,64,4,3]

for m in range(0,len(array)):
    for n in range(1,len(array)):
        if(array[n]>array[n-1]):
            temp = array[n-1]
            array[n-1] = array[n]
            array[n]=temp
print(array)
print(f'The second largest number in an array is {array[1]}')