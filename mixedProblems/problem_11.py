# Problem 10 :How to check if a given number is an Armstrong number ?
text = input("Enter your number: ")
number = int(text)
numberArray = []
for i in text:
    numberArray.append(int(i))

sum=0
count=1
for x in numberArray:
    for y in range(3):
        count = count*x

    sum = sum+count
    count=1

if(sum==number):
    print("The Number is an Armstrong number")
else:
    print("The Number is not an Armstrong number")
