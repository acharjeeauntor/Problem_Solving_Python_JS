# Problem 5 : How do you check if the given number is prime?


def isPrime(number):
    if(number==0 or number==1):
        return False
    if(number==2):
        return True
    for m in range(2,number):
        if(number%m==0):
            return False
    return True

num = int(input("Enter Your Number: "))
print(isPrime(num))