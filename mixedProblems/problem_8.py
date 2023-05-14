# Problem 8 : How do you swap two numbers without using the third variable?

firstNumber = int(input("Enter First Number: "))
secondNumber = int(input("Enter Second Number: "))

afterSwapFirstNumber = (firstNumber+secondNumber)-firstNumber
afterSwapSecondNumber = (firstNumber+secondNumber)-secondNumber

print(f'After Swap: First Number is {afterSwapFirstNumber} and Second Number is {afterSwapSecondNumber}')