# Problem 4 : How do you find the maximum occurring character in a given string?

text = input("Enter your String: ")

index=0
count=0
lastHeighestValue=0

for x in range(0,len(text)):
    for y in range(x+1,len(text)):
        if(text[x]==text[y]):
            count+=1
    if(count>lastHeighestValue):
        lastHeighestValue=count
        count=0
        index=x

if(lastHeighestValue==0):
    print("There are no maximum occurring character in the given string")
else:
 print(f"Maximum occurring character in the given string is {text[index]}")

