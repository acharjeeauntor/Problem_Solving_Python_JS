# Problem 4 : How do you find the maximum occurring character in a given string?

text = input("Enter your String: ")
count=0
for x in text:
    for y in text:
        if(x==y):
            count+=1
    print(f"{x} = {count}")
    count=0
