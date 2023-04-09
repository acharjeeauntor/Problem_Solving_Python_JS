################################# Variables



# patient_name = "Auntor"
# age = 25
# is_new_patient = False

# print(f"{patient_name} is {age} years old. Is he is a new patient?: {is_new_patient}")


################################# Receiving Input
# Note:
# input function always return a String.




# name = input("What is you name? ")
# print('Hello '+name)


################################# Type Conversion
# Note:
# Those are built-in type conversion function. 
# int()
# str()
# float()
# bool()

# birth_date = input("What is your birth date? ")
# age = 2023-int(birth_date)
# print(f"Your age is: {age}")
# print(type(age))
# age = age+0.5
# print(int(age))
# age=float(age)
# print(type(age))
# print(age)
# age = str(age)
# print(type(age))
# print(age)

# isTrue = "True"
# print(type(isTrue))
# isTrue = bool(isTrue)
# print(isTrue)
# print(type(isTrue))


# Sum Two number
# first_number = float(input("Enter First  Number: "))
# second_number = float(input("Enter Second Number: "))
# sum = first_number + second_number
# print(sum)

################################# String

# text = "I Love BD"
# print(text.capitalize())
# print(text.lower())
# print(text.upper())
# print(text.find("L"))
# print(text.find('BD'))
# print(text.replace('BD','You'))
# # print(text.count())
# print(text.split(" "))
# print('BD' in text)

################################# Arithmatic Operator
# x = 10
# y = 5

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)
# print(x%y)
# print(x**y) # x*x*x*x*X

# x=x+9
# print(x)
# y+=8
# print(y)

################################# Operator Precedence
# x = 10 + 3 * 2  # Order: /,*,+,-
# print(x)

# y = (10 + 3) * 2
# print(y)

################################# Comparision Operator
# Type: <,<=,>,>=,==,!=

# x = 3<2
# print(x)
# y = 3<=2
# print(y)
# z = 3>=2
# print(z)
# a = 3>2
# print(a)
# b = 3==2
# print(b)
# c = 3!=2
# print(c)

################################# Logical Operator

# x = 10
# print(x>20 or x<30)
# print(x>20 and x<30)
# print(x>20)
# print(not x>20)

################################# if else Statement

# temp = 22

# if temp>30:
#     print("It's Hot today")
# elif temp>20:
#     print("Its less Hot today")
# else:
#     print("Its bit cold today")
# print("Done")
    

################################# while loop

# i = 1
# while i<=10:
#     print(i * '#')
#     i+=1


################################# For loop
# info = ["Auntor",25,"Tangail","DIU","Brotecs",1998]

# for item in info:
#     print(item)
#     if (item == 25):
#         print("item is your age.")


################################# List/Array

# info = ["Auntor",25,"Tangail","DIU","Brotecs",1998]
# print(info)
# print(info[0])
# print(info[-1])
# print(info[-2])
# info[0] = "Ontu"
# print(info)
# print(info[0:4])

################################# List Methods

# numbers = [1,3,4,7,9,2]
# numbers.append(0)
# print(numbers)
# numbers.insert(1,50)
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.remove(7)
# print(numbers)
# print(len(numbers))
# numbers.extend([5,6])
# print(numbers)
# print(51 in numbers)
# numbers.clear()
# print(numbers)

################################# Range Function
# numbers = range(5,10)
# for num in numbers:
#     print(num)

# for num in range(5,20):
#     print(num)

# for num in range(5,20,3):
#     print(num)

################################# Tuples
# Tuples unchangable / emutable

# numbers = (2,5,6,7,9,3,6)
# print(numbers.count(6))
# print(numbers.index(7))

################################# 2D List

# matrix = [
# [4,5,6],
# [10,11,12],
# [15,16,17]
# ]

# # print(matrix[0][1])
# for row in matrix:
#     for item in row:
#         print(item)

################################# Unpacking
# unpacking mainly List r Tuples e use kora jay. Tuples r List er value gulo k use krte amra unpacking 
# use korte pari

# exampleTuples = (5,8,9)
# exampleList= [55,88,99]

# x,y,z=exampleTuples
# a,b,c=exampleList

# print(b,z)

################################# Dictionaries
# customer = {
#     "name":"Auntor",
#     "age":25,
#     "is_married":False
# }
# print(customer["age"])
# customer["company"] = "Brotecs"
# print(customer["company"])
# customer["name"] = "Ontu"
# print(customer)

################################# Function

# def user_info(fName,lName):
#     print(f"Your First Name is {fName}")
#     print(f"Your Last Name is {lName}")

# print("start")
# user_info("Auntor","Acharja")
# print("stop")


#### Keyword Argument Function [parameter e keyword add kore deya jay.]

# def user_info(fName,lName):
#     print(f"Your First Name is {fName}")
#     print(f"Your Last Name is {lName}")

# print("start")
# user_info(fName="Auntor",lName="Acharja")
# print("stop")

# print("start")
# user_info("Ontu",lName="Acharja")
# print("stop")

#### Return Function

# def squre(number):
#     return number*number

# result = squre(6)
# print(result)