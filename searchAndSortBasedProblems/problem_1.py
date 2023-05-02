# Problem 1 - How do you write a program that sorts numbers?

array = [2,4,5,1,6,8,0,3,7]

for j in range(0,len(array)):
    for i in range(1,len(array)):
        if(array[i]<array[i-1]):
            temp = array[i-1]
            array[i] = array[i-1]
            array[i-1] = temp

print(array)