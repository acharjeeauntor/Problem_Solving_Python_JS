# Problem 4 : How do you find the factorial of an integer?

# def factorial(n):
#     if(n==1):
#         return 1
#     else:
#         return (n*factorial(n-1))
    

# print(factorial(1))


def factorial(n):
    y=1
    if(n==1):
        return 1
    else:
        for x in range(5,0,-1):
            y=y*x
        return y

    

print(factorial(1))