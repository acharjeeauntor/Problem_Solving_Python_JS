// Problem 8 : How do you swap two numbers without using the third variable?

var firstNumber = 10
var secondNumber = 20

var afterSwapSecondNumber = (firstNumber+secondNumber)-secondNumber
var afterSwapFirstNumber = (firstNumber+secondNumber)-firstNumber

console.log(`After Swapping: First number is ${afterSwapFirstNumber} and Second Number is ${afterSwapSecondNumber}`)