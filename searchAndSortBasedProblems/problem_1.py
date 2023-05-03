# Problem 1 - How do you write a program that sorts numbers?

array = [2,4,5,1,6,8,0,3,7]

# First Way
# for i in range(0,len(array)):
#     for j in range(i+1,len(array)):
#         if(array[i]>array[j]):
#             temp = array[i]
#             array[i] = array[j]
#             array[j] = temp

# print(array)

# Second Way
for j in range(0,len(array)):
    for i in range(1,len(array)):
        if(array[i]<array[i-1]):
            temp = array[i-1]
            array[i-1]=array[i]
            array[i] = temp
print(array)