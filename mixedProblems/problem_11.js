// Problem 10 :How to check if a given number is an Armstrong number ?
var number = 153
var arrayOfNumber = number.toString().split('')
sum = 0
for(var i =0;i<arrayOfNumber.length;i++){
    var n = parseInt(arrayOfNumber[i])
    var cubeOfNumber = n*n*n
    sum+=cubeOfNumber
}
if(sum==number){
    console.log("The number is Armstrong number")
}else{
    console.log("The number is not Armstrong number")
}