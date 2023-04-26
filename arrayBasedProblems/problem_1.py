# Problem 1 : How do you find the largest and smallest number in an array of 1-100?

# 1st Way
# array =[]
# for x in range(1,100+1):
#     array.append(x)

# for x in range(0,len(array)):
#     for y in range(1,len(array)):
#         if(array[y] < array[y-1]):
#             temp = array[y]
#             array[y] = array[y-1]
#             array[y-1] = temp

# print(f"The largest number in an array is {array[len(array)-1]}")
# print(f"The smallest number in an array is {array[0]}")


# 2nd Way
array =[4,5,8,9,1,4,7,40,2,0,2,3]
newArray = sorted(array)

print(f"The largest number in an array is {newArray[len(newArray)-1]}")
print(f"The smallest number in an array is {newArray[0]}")