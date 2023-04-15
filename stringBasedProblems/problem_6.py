# Problem 6 : How do you split a string in python?

#### 1st Way
text = input("Please enter your String: ")
splitedString = []
for word in text:
    splitedString.append(word)

print(splitedString)


#### 2nd Way
text = input("Please enter your String: ")
splitedString = text.split(' ')
print(splitedString)


