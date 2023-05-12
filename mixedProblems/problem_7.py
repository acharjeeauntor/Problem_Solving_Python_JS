# Problem 7: How do you calculate the number of vowels and consonants in a String?

myString = input("Enter your string: ")
lowerString = myString.lower()

vowelCount = 0
consonantCount = 0
for word in lowerString:
    if word=='a' or word =='e' or word=='i' or word=='o' or word=='u':
        vowelCount+=1
    else:
        consonantCount+=1

print(f'Total vowel: {vowelCount} and Total consonant: {consonantCount}')