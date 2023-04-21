# Problem 2: How do you calculate the number of vowels and consonants in a String

myString = input("Enter your desier String: ")
text = myString.lower()
noOfVowel = 0
noOfCons = 0

for word in text:
    if(word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u'):
        noOfVowel+=1
    else:
        noOfCons+=1

print(f"Number of Vowel is {noOfVowel} and Number of Consonant is {noOfCons}")