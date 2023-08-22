// Problem 5 : How do you check if the given number is prime?

function isPrimeNumber(number){
if(number==0 || number==1){
   return false
}else if(number==2){
    return true
}
for(var i=2;i<=number;i++){
    if(number%i==0){
        return false
    }
}
return true
}

var result  = isPrimeNumber(6)
if(result===true){
    console.log("The given number is prime number")
}else if(result===false){
    console.log("The given number is not a prime number")
}
