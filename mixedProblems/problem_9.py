# Problem 9 : How do you check if a string contains only digits?
import re
text = input("Enter the text: ")
totalCharOfText = len(text)
arrayOfNumberInText = re.findall("[0-9]",text)
totalNumberInText = len(arrayOfNumberInText)
if(totalCharOfText==totalNumberInText):
    print("String contains only digits")
else:
    print("String is not contains only digits")

