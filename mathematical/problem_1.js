// Problem 1 : Check if a large number is divisible by 3 or not [A number is divisible by 3 if sum of its digits is divisible by 3]

var number = 347864394877777665987
var sum = 0
var arrayOFNumber = number.toString().split('')
console.log(arrayOFNumber)
for(var i = 0 ;i<arrayOFNumber.length;i++){
sum = sum+parseInt(arrayOFNumber[i])
}
console.log(sum)
if(sum%3==0){
    console.log("The number is divisible by 3")
}else{
    console.log("The number is not divisible by 3")
}