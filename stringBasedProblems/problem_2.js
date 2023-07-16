// Problem 2 : How can you write a code to check if a string is a palindrome or not?

function myfunc(text){
var arrayOfString = text.split('')
var reverseString = ""
for (var i=arrayOfString.length-1;i>=0;i--){
    reverseString+=arrayOfString[i]
}

if(text==reverseString){
    console.log("The String is palindrome")
}else{
    console.log("The String is not palindrome")
}
}

myfunc("5115")