# Problem 5 : How do you find the first unrepeated character of a given string?

text = input("Enter your Text: ")

for i in range(0,len(text)):
    count = 0
    for j in range(i+1,len(text)):
        if(text[i]==text[j]):
            count+=1
    if(count==0):
        print(text[i])
        break