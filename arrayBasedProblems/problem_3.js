// Problem 3: How do you reverse an array in place in js?

var oldArray=[5,8,9,4,10,5,3,7]
var reversedArray = []
for(var i =oldArray.length-1;i>=0;i--){
reversedArray.push(oldArray[i])
}
console.log(reversedArray)