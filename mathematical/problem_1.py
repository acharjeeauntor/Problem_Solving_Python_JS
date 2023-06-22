# Problem 1 : Check if a large number is divisible by 3 or not [A number is divisible by 3 if sum of its digits is divisible by 3]

text = input("Enter the number: ")
sum=0

for n in text:
    sum = sum+int(n)
print(sum)
if sum%3 ==0:
    print("Yes")
else:
    print("No")