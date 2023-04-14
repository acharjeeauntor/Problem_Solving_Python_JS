# Problem 2 : How can you write a code to check if a string is a palindrome or not?

#### 1st Way
text = input("Please enter your String: ")
firstList = []
reversedList = []
reversedText=""

for word in text:
    firstList.append(word)


for word in firstList[::-1]:
    reversedList.append(word)

for word in reversedList:
    reversedText+=word

if(text==reversedText):
    print("The text you entered is a palindrome")
else:
    print("The text you entered is not a palindrome")



#### 2nd Way
text = input("Please enter your String: ")
reversedList = []
reversedText=""

firstList = list(text)

for word in reversed(firstList):
    reversedList.append(word)

for word in reversedList:
    reversedText+=word

if(text==reversedText):
    print("The text you entered is a palindrome")
else:
    print("The text you entered is not a palindrome")
