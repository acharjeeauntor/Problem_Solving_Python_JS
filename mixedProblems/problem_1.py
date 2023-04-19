# Problem 1 : How do you reverse a string in Python?

text = input("Enter your desired String: ")
reversedString=""
textList = list(text)
for word in textList[::-1]:
    reversedString+=word

print(reversedString)