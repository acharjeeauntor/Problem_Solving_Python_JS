// Problem 1 : How do you reverse a string in js?


var myString = "Auntor"
var arrOfString = myString.split("")
var reverseString=""
for(var i=arrOfString.length-1;i>=0;i--){
    reverseString+=arrOfString[i]
}
console.log(reverseString)

// 2nd way

// var myString = "Auntor"
// var reverseString=myString.split("").reverse().join("")
// console.log(reverseString)


// Join a array in js
var x = ["4","e","a"]
console.log(x.join(""))